from uuid import UUID
from dataclasses import dataclass

from notification.domain.settings.value_object import NotificationChannel


@dataclass
class SettingsCreateRequestDTO:
    user_id: UUID
    notification_channel: NotificationChannel = NotificationChannel.EMAIL
    enabled_notifications: bool = True
    email: str | None = None
    telegram_id: int | None = None

    def __post_init__(self):
        if (self.email is None) and (self.telegram_id is None):
            raise ValueError("Must provide email or telegram_id")


@dataclass
class SettingsCreateResponseDTO:
    user_id: UUID
    notification_channel: NotificationChannel = NotificationChannel.EMAIL
    enabled_notifications: bool = True


@dataclass
class SettingsDeleteRequestDTO:
    user_id: UUID
