from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from notification_service.setup.config import config


engine = create_async_engine(
    url=config.db.URL,
    pool_size=config.alchemy.POOL_SIZE,
)
async_session = async_sessionmaker(
    engine,
    expire_on_commit=config.alchemy.EXPIRE_ON_COMMIT,
    autoflush=config.alchemy.AUTOFLUSH,
)
