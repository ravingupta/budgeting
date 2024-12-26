from typing import Optional
from sqlmodel import Field, Session, select, UniqueConstraint

from config import appConfig

from .base import BaseModel

class Transaction(BaseModel, table=True):
    __table_args__ = (
        UniqueConstraint("date", "description", "amount", name="trasaction_uc"),
    )
    account_id: int = Field(foreign_key='account.id')
    date: str = Field()
    description: str = Field()
    amount: float = Field()
    type: Optional[str] = Field(default=None)
    category: Optional[str] = Field(default=None, index=True, foreign_key="category.id")
    tags: Optional[str] = Field(default=None)
    notes: Optional[str] = Field(default=None)

    def __str__(self):
        return f'{self.date} | {self.description} | {self.amount} | {self.type}'
    
    def __repr__(self):
        return f'{self.date} | {self.description} | {self.amount} | {self.type}'

def db_get_transactions(account_id: int = None):
    with Session(appConfig.connection) as session:
        if account_id:
            statement = select(Transaction).where(Transaction.account_id == account_id)
            result = session.exec(statement)
            return result.fetchall()
        return []

def db_add_transaction(account_id: int, date: str, description: str, amount: float, type: str):
    trasaction = Transaction(account_id = account_id, date = date, description = description, amount = amount, type = type)
    trasaction.create()
    return trasaction