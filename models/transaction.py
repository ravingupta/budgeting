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
    
def db_get_transaction(account_id: int, transaction_id: int):
    with Session(appConfig.connection) as session:
        statement = select(Transaction).where(Transaction.account_id == account_id, Transaction.id == transaction_id)
        result = session.exec(statement)
        return result.first()
    
def db_update_transaction(description: str, category: str):
    with Session(appConfig.connection) as session:
        statement = select(Transaction).where(Transaction.description == description)
        result = session.exec(statement)
        transaction = result.fetchall()
        if len(transaction) == 0:
            return False
        for t in transaction:
            t.category = category
            session.add(t)
        session.commit()
        return True

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