from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from faststream import FastStream
from pydantic import AmqpDsn

from notification.presentation.http.api_router import api_router
from notification.presentation.broker.routers import settings_router
from notification.infrastructure.broker.rabbitmq_broker import create_rabbitmq_broker
from notification.setup.config import config
from notification.setup.di import (
    create_fastapi_dishka,
    create_faststream_dishka,
    get_providers,
    crate_dishka_container,
)


def create_faststream_app(url: AmqpDsn = config.rabbitmq.URL) -> FastStream:
    broker = create_rabbitmq_broker(url)
    app = FastStream(broker)
    providers = get_providers()
    container = crate_dishka_container(providers)
    create_faststream_dishka(app=app, container=container)
    broker.include_routers(settings_router)
    # TODO add Context Config
    return app


@asynccontextmanager
async def broker_lifespan(app: FastAPI) -> AsyncIterator[None]:
    async with create_faststream_app():
        yield


def create_fastapi_app() -> FastAPI:
    app = FastAPI(lifespan=broker_lifespan)
    app.include_router(api_router)
    providers = get_providers()
    container = crate_dishka_container(providers)
    create_fastapi_dishka(app=app, container=container)
    # TODO add Context Config
    return app
