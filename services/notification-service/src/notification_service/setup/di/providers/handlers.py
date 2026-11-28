from dishka import Provider, provide, Scope

from notification_service.application.ports.database.inbox import Inbox
from notification_service.application.ports.database.repositories.settings import SettingsRepository
from notification_service.application.ports.database.tx_manager import TxManager
from notification_service.application.handlers.settings import (
    SettingsCreateHandler,
    SettingsDeleteHandler,
)



class HandlerProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def get_create_settings_handler(
        self,
        settings_repository: SettingsRepository,
        tx_manager: TxManager,
        inbox: Inbox,
    ) -> SettingsCreateHandler:
        return SettingsCreateHandler(
            settings_repository=settings_repository,
            tx_manager=tx_manager,
            inbox=inbox,
        )

    @provide
    async def get_delete_settings_handler(
        self,
        settings_repository: SettingsRepository,
        tx_manager: TxManager,
    ) -> SettingsDeleteHandler:
        return SettingsDeleteHandler(
            settings_repository=settings_repository,
            tx_manager=tx_manager,
        )
