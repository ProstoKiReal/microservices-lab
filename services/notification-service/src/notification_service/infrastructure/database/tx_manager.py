from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession

from notification_service.application.ports.database.tx_manager import TxManager


class AlchemyTxManager(TxManager):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self) -> Self:
        if not self.session.in_transaction():
            await self.session.begin().start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            await self.session.rollback()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
