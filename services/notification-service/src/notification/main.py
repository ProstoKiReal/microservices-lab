from fastapi import FastAPI

from notification.setup import create_fastapi_app


def create_app() -> FastAPI:
    return create_fastapi_app()
