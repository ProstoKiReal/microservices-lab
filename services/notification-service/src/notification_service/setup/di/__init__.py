from notification_service.setup.di.setup import (
    crate_dishka_container,
    create_fastapi_dishka,
    create_faststream_dishka,
    get_dishka_context,
)
from notification_service.setup.di.providers.registry import get_providers


__all__ = [
    "crate_dishka_container",
    "create_fastapi_dishka",
    "create_faststream_dishka",
    "get_providers",
    "get_dishka_context",
]
