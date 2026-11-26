from faststream.rabbit.broker import RabbitBroker
from pydantic import AmqpDsn


def create_rabbitmq_broker(url: AmqpDsn) -> RabbitBroker:
    return RabbitBroker(url=str(url))
