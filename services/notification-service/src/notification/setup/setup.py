from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from faststream import FastStream
from pydantic import AmqpDsn

from notification.presentation.http.api_router import api_router
from notification.infrastructure.broker.rabbitmq_broker import create_rabbitmq_broker
from notification.setup.config import config


def create_faststream_app(url: AmqpDsn = config.rabbitmq.URL) -> FastStream:
    broker = create_rabbitmq_broker(url)
    app = FastStream(broker)
    return app


@asynccontextmanager
async def broker_lifespan(app: FastAPI) -> AsyncIterator[None]:
    async with create_faststream_app():
        yield


def create_fastapi_app() -> FastAPI:
    app = FastAPI(lifespan=broker_lifespan)
    app.include_router(api_router)
    return app
