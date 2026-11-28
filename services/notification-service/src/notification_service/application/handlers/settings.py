from notification_service.application.handlers.scopes import InboxScope
from notification_service.application.ports.database.inbox import Inbox
from notification_service.application.ports.database.repositories import SettingsRepository
from notification_service.application.ports.database.tx_manager import TxManager
from notification_service.application.dtos.settings import SettingsCreateRequestDTO, SettingsDeleteRequestDTO, SettingsCreateResponseDTO
from notification_service.domain.settings.entities import Settings


class SettingsCreateHandler:
    def __init__(
        self,
        settings_repository: SettingsRepository,
        tx_manager: TxManager,
        inbox: Inbox,
    ):
        self.settings_repository = settings_repository
        self.tx_manager = tx_manager
        self.inbox = inbox

    async def __call__(self, settings_dto: SettingsCreateRequestDTO) -> SettingsCreateResponseDTO | None:
        async with self.tx_manager:
            if not await self.inbox.claim(
                scope=InboxScope.USERS_CREATE,
                message_id=str(settings_dto.user_id),
            ):
                return None
            user_settings = await self.settings_repository.get_by_user(settings_dto.user_id)
            if user_settings is None:
                settings_domain = self.to_domain(settings_dto)
                created = await self.settings_repository.add(settings_domain)
                await self.tx_manager.commit()
                return self.to_dto(created)
            return self.to_dto(user_settings)

    @staticmethod
    def to_domain(dto: SettingsCreateRequestDTO) -> Settings:
        return Settings(
            id=dto.user_id,
            user_id=dto.user_id,
            notification_channel=dto.notification_channel,
            enabled_notifications=dto.enabled_notifications,
            email=dto.email,
            telegram_id=dto.telegram_id,
        )

    @staticmethod
    def to_dto(domain: Settings) -> SettingsCreateResponseDTO:
        return SettingsCreateResponseDTO(
            user_id=domain.user_id,
            notification_channel=domain.notification_channel,
            enabled_notifications=domain.enabled_notifications,
        )


class SettingsDeleteHandler:
    def __init__(
        self,
        settings_repository: SettingsRepository,
        tx_manager: TxManager,
    ):
        self.settings_repository = settings_repository
        self.tx_manager = tx_manager

    async def __call__(self, settings_dto: SettingsDeleteRequestDTO) -> bool:
        async with self.tx_manager:
            deleted = await self.settings_repository.delete(settings_dto.user_id)
            await self.tx_manager.commit()
            return deleted
