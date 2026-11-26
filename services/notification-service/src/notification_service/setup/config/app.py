from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="NOTIFICATION_APP_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    PORT: int
    HOST: str
    MODE: str

    @property
    def DEBUG(self) -> bool:
        if self.MODE == "dev":
            return True
        return False
