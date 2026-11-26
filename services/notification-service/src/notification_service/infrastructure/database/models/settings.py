from dataclasses import dataclass
from uuid import UUID

from notification_service.domain.settings.value_object import NotificationChannel
from notification_service.infrastructure.database.models.registry import mapper_registry

from sqlalchemy import Table, Column, Enum, Boolean, String, BigInteger, UUID as SaUUID


@dataclass
class SettingsModel:
    id: UUID
    user_id: UUID
    channel: NotificationChannel
    email: str
    telegram_id: int
    notification_enabled: bool


settings_table = Table(
    "settings",
    mapper_registry.metadata,
    Column("id", SaUUID, primary_key=True),
    Column("user_id", SaUUID),
    Column("channel", Enum(NotificationChannel), nullable=False, default=NotificationChannel.EMAIL),
    Column("email", String, nullable=True, unique=True),
    Column("telegram_id", BigInteger, nullable=True, unique=True),
    Column("notification_enabled", Boolean, default=True),
)

mapper_registry.map_imperatively(SettingsModel, settings_table)
