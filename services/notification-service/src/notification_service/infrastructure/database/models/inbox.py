from faststream_outbox import make_outbox_table

from notification_service.infrastructure.database.models.registry import mapper_registry


outbox_table = make_outbox_table(mapper_registry.metadata, table_name="inbox")
