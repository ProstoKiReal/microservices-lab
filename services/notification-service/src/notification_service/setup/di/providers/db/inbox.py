from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_inbox import Inbox as AlchemyInbox

from notification_service.application.ports.database.inbox import Inbox
from notification_service.infrastructure.database.models.inbox import inbox_table


class InboxProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_inbox(self, session: AsyncSession) -> Inbox:
        return AlchemyInbox(session, table=inbox_table)
