import re
from uuid import UUID
from dataclasses import dataclass

from notification_service.domain.settings.value_object import NotificationChannel
from notification_service.domain.settings.errors import TelegramIdDomainError, EmailDomainError, NotExistedNotificationChannelDomainError


@dataclass
class Settings:
    id: UUID
    user_id: UUID
    notification_channel: NotificationChannel
    enabled_notifications: bool = True
    email: str | None = None
    telegram_id: int | None = None

    def __post_init__(self):
        if self.email is not None:
            self._validate_email()
        if self.telegram_id is not None:
            self._validate_telegram_id()
        self._validate_notification_values()

    def _validate_email(self) -> None:
        if self.email is None:
            return

        pattern = re.compile(
            r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+"
            r"@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
            r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
        )
        match = re.match(pattern, self.email)
        if not match:
            raise EmailDomainError(self.email)

    def _validate_telegram_id(self) -> None:
        if self.telegram_id is not None and self.telegram_id < 0:
            raise TelegramIdDomainError(self.telegram_id)

    def _validate_notification_values(self) -> None:
        if not self.email and not self.telegram_id:
            raise NotExistedNotificationChannelDomainError
