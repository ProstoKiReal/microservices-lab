from notification_service.setup.di.setup import (
    crate_dishka_container,
    create_fastapi_dishka,
    create_faststream_dishka,
)
from notification_service.setup.di.providers.registry import get_providers


__all__ = [
    "crate_dishka_container",
    "create_fastapi_dishka",
    "create_faststream_dishka",
    "get_providers",
]
