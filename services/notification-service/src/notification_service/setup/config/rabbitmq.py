from pydantic import SecretStr, AmqpDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RabbitMQConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="RABBITMQ_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    USER: str
    HOST: str
    PORT: int
    PASSWORD: SecretStr

    @property
    def URL(self) -> AmqpDsn:
        return AmqpDsn(
            f"amqp://{self.USER}:{self.PASSWORD.get_secret_value()}@{self.HOST}:{self.PORT}/"
        )
