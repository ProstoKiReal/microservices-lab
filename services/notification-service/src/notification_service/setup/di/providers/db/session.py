from typing import AsyncGenerator

from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from notification_service.infrastructure.database.database import (
    create_async_engine,
    create_async_sessionmaker,
)
from notification_service.setup.config import config


class DBEngineProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_engine(self) -> AsyncGenerator[AsyncEngine]:
        engine = create_async_engine(
            url=config.db.URL,
            pool_size=config.alchemy.POOL_SIZE,
        )
        yield engine
        await engine.dispose()

    @provide
    def get_session_maker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return create_async_sessionmaker(
            engine=engine,
            expire_on_commit=config.alchemy.EXPIRE_ON_COMMIT,
            autoflush=config.alchemy.AUTOFLUSH,
        )


class DBSessionProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def get_db_session(self, session_maker: async_sessionmaker[AsyncSession]) -> AsyncGenerator[AsyncSession]:
        async with session_maker() as session:
            yield session
