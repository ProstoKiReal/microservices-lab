from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import  AsyncSession

from notification.application.ports.database.tx_manager import TxManager
from notification.infrastructure.database.tx_manager import AlchemyTxManager


class TXMangerProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def get_tx_manager(self, session: AsyncSession) -> TxManager:
        return AlchemyTxManager(session=session)
