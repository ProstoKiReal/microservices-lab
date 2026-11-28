from typing import Protocol
from abc import abstractmethod


class Inbox(Protocol):
    @abstractmethod
    async def claim(self, *, scope: str, message_id: str) -> bool: ...
