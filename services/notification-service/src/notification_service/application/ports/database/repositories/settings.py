from uuid import UUID
from abc import abstractmethod
from typing import Protocol

from notification_service.domain.settings.entities import Settings


class SettingsRepository(Protocol):
    @abstractmethod
    async def get_by_user(self, user_id: UUID) -> Settings | None: ...

    @abstractmethod
    async def add(self, settings: Settings) -> Settings: ...

    @abstractmethod
    async def update(self, settings: Settings) -> Settings: ...

    @abstractmethod
    async def delete(self, user_id: UUID) ->  bool: ...
