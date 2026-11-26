from uuid import UUID

from notification_service.application.ports.database.repositories import SettingsRepository
from notification_service.domain.settings.entities import Settings
from notification_service.infrastructure.database.models.settings import SettingsModel

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete


class AlchemySettingsRepository(SettingsRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_user(self, user_id: UUID) -> Settings | None:
        query = select(SettingsModel).where(SettingsModel.user_id == user_id).limit(1)
        req = await self.session.execute(query)
        return self._to_domain(req.scalar_one_or_none())

    async def add(self, settings: Settings) -> Settings:
        model = self._to_model(settings)
        self.session.add(model)
        return settings

    async def update(self, settings: Settings) -> Settings:
        raise NotImplementedError()

    async def delete(self, user_id: UUID) ->  bool:
        stmt = delete(SettingsModel).where(SettingsModel.user_id == user_id)
        await self.session.execute(stmt)
        if not await self.get_by_user(user_id):
            return True
        return False

    @staticmethod
    def _to_domain(settings: SettingsModel | None) -> Settings | None:
        if settings is None:
            return None
        return Settings(
            id=settings.id,
            user_id=settings.user_id,
            notification_channel=settings.channel,
            enabled_notifications=settings.notification_enabled,
            email=settings.email,
            telegram_id=settings.telegram_id,
        )

    @staticmethod
    def _to_model(settings: Settings) -> SettingsModel:
        return SettingsModel(
            id=settings.id,
            user_id=settings.user_id,
            channel=settings.notification_channel,
            email=settings.email,
            telegram_id=settings.telegram_id,
            notification_enabled=settings.enabled_notifications,
        )
