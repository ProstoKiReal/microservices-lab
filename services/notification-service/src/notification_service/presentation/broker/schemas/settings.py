from uuid import UUID

from pydantic import BaseModel, Field, EmailStr, model_validator

from notification_service.domain.settings.value_object import NotificationChannel


class SettingsCreateRequest(BaseModel):
    user_id: UUID
    notification_channel: NotificationChannel = Field(default=NotificationChannel.EMAIL)
    enabled_notifications: bool = Field(default=True)
    email: EmailStr | None = Field(default=None)
    telegram_id: int | None = Field(default=None)

    @model_validator(mode="after")
    def validate_notification_channel(self):
        if (self.email is None) and (self.telegram_id is None):
            raise ValueError("Must provide email or telegram_id")
        return self


class SettingsDeleteRequest(BaseModel):
    user_id: UUID
