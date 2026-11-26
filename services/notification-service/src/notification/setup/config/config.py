from notification.setup.config.rabbitmq import RabbitMQConfig
from notification.setup.config.db import DBConfig
from notification.setup.config.app import AppConfig
from notification.setup.config.alchemy import AlchemyConfig


class Config:
    rabbitmq: RabbitMQConfig = RabbitMQConfig()
    db: DBConfig = DBConfig()
    app: AppConfig = AppConfig()
    alchemy: AlchemyConfig = AlchemyConfig()


config = Config()
