from typing import Iterable, Any

from fastapi import FastAPI
from faststream import FastStream
from dishka import Provider, make_async_container, Container
from dishka.integrations.fastapi import setup_dishka as fastapi_setup_dishka
from dishka_faststream import setup_dishka as faststream_setup_dishka

from notification_service.setup.config import Config, config


def crate_dishka_container(providers: Iterable[Provider], context: dict[Provider,Any]):
    container = make_async_container(*providers, context=context)
    return container


def create_fastapi_dishka(app: FastAPI, container: Container) -> None:
    fastapi_setup_dishka(app=app, container=container,)


def create_faststream_dishka(app: FastStream, container: Container) -> None:
    faststream_setup_dishka(app=app, container=container, auto_inject=True)


def get_dishka_context():
    return {
        Config: config,
    }