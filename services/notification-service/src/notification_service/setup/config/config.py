from notification_service.setup.config.rabbitmq import RabbitMQConfig
from notification_service.setup.config.db import DBConfig
from notification_service.setup.config.app import AppConfig
from notification_service.setup.config.alchemy import AlchemyConfig


class Config:
    rabbitmq: RabbitMQConfig = RabbitMQConfig()
    db: DBConfig = DBConfig()
    app: AppConfig = AppConfig()
    alchemy: AlchemyConfig = AlchemyConfig()


config = Config()
