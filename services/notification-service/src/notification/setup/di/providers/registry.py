from typing import Iterable

from dishka import Provider

from notification.setup.di.providers import (
    DBSessionProvider,
    RepositoryProvider,
    TXMangerProvider,
    BrokerAuthProvider,
    HttpAuthProvider,
    HandlerProvider,
)


def get_providers() -> Iterable[Provider]:
    return [
    DBSessionProvider(),
    RepositoryProvider(),
    TXMangerProvider(),
    BrokerAuthProvider(),
    HttpAuthProvider(),
    HandlerProvider(),
    ]
