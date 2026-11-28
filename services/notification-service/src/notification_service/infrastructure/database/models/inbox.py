from sqlalchemy_inbox import make_inbox_table

from notification_service.infrastructure.database.models.registry import mapper_registry


inbox_table = make_inbox_table(mapper_registry.metadata, table_name="inbox")
