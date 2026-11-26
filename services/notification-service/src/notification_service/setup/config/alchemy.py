from pydantic_settings import BaseSettings, SettingsConfigDict


class AlchemyConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="NOTIFICATION_ALCHEMY_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    POOL_SIZE: int
    AUTOFLUSH: bool
    EXPIRE_ON_COMMIT: bool
