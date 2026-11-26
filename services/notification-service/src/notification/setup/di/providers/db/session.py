from typing import AsyncGenerator

from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import  AsyncSession

from notification.infrastructure.database.database import async_session


class DBSessionProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def get_db_session(self) -> AsyncGenerator[AsyncSession]:
        async with async_session() as session:
            yield session
