from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession

from notification.application.ports.database.repositories.settings import SettingsRepository
from notification.infrastructure.database.repositories.settings import AlchemySettingsRepository


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def get_settings_repository(self, session: AsyncSession) -> SettingsRepository:
        return AlchemySettingsRepository(session)
