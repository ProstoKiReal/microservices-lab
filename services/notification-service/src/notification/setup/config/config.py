from notification.setup.config.rabbitmq import RabbitMQConfig


class Config:
    rabbitmq: RabbitMQConfig = RabbitMQConfig()


config = Config()
