from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from faststream import FastStream
from pydantic import AmqpDsn

from notification_service.presentation.http.api_router import api_router
from notification_service.presentation.broker.routers import settings_router
from notification_service.infrastructure.broker.broker import (
    create_rabbitmq_broker,
)
from notification_service.setup.config import config, Config
from notification_service.setup.di import (
    create_fastapi_dishka,
    create_faststream_dishka,
    crate_dishka_container,
    get_dishka_context,
    get_providers,

)


def create_faststream_app(url: AmqpDsn = config.rabbitmq.URL) -> FastStream:
    broker = create_rabbitmq_broker(url)
    app = FastStream(broker)
    providers = get_providers()
    context = get_dishka_context()
    container = crate_dishka_container(providers=providers, context=context)
    create_faststream_dishka(app=app, container=container)
    broker.include_routers(settings_router)
    return app


@asynccontextmanager
async def broker_lifespan(app: FastAPI) -> AsyncIterator[None]:
    async with create_faststream_app():
        yield


def create_fastapi_app() -> FastAPI:
    app = FastAPI(lifespan=broker_lifespan)
    app.include_router(api_router)
    providers = get_providers()
    context = get_dishka_context()
    container = crate_dishka_container(providers=providers, context=context)
    create_fastapi_dishka(app=app, container=container)
    return app
