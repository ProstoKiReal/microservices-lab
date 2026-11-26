from fastapi import FastAPI

from notification_service.setup import create_fastapi_app


def create_app() -> FastAPI:
    return create_fastapi_app()
