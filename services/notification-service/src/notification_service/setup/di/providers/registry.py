from typing import Iterable

from dishka import Provider

from notification_service.setup.di.providers import (
    DBEngineProvider,
    DBSessionProvider,
    InboxProvider,
    RepositoryProvider,
    TXMangerProvider,
    BrokerAuthProvider,
    HttpAuthProvider,
    HandlerProvider,
)


def get_providers() -> Iterable[Provider]:
    return [
    DBEngineProvider(),
    DBSessionProvider(),
    InboxProvider(),
    RepositoryProvider(),
    TXMangerProvider(),
    BrokerAuthProvider(),
    HttpAuthProvider(),
    HandlerProvider(),
    ]
