from pydantic import SecretStr, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="NOTIFICATION_DB_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    USER: str
    NAME: str
    HOST: str
    PORT: int
    PASSWORD: SecretStr

    @property
    def URL(self) -> str:
        return str(
            PostgresDsn(
                f"postgresql+asyncpg://{self.USER}:{self.PASSWORD.get_secret_value()}@{self.HOST}:{self.PORT}/{self.NAME}"
            )
        )
