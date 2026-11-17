from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field


class NotificationChannel(Enum):
    EMAIL = "email"
    TG  = "tg"


class UserCreateRequest(BaseModel):
    user_id: UUID
    notification_channel: NotificationChannel = Field(NotificationChannel.EMAIL)
    enabled_notifications: bool = Field(True)


class UserDeleteRequest(BaseModel):
    user_id: UUID
