from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine as sa_create_async_engine,
)


def create_async_engine(url: str, pool_size: int) -> AsyncEngine:
    return sa_create_async_engine(
        url=url,
        pool_size=pool_size,
    )


def create_async_sessionmaker(
    engine: AsyncEngine,
    expire_on_commit: bool,
    autoflush: bool,
) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(
        engine,
        expire_on_commit=expire_on_commit,
        autoflush=autoflush,
    )
