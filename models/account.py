from sqlmodel import Field, Session, select, UniqueConstraint

from config import appConfig

from .base import BaseModel

class Account(BaseModel, table=True):
    __table_args__ = (
        UniqueConstraint("bank", "name", name="account_uc"),
    )
    bank: str = Field(default=None, index=True)
    name: str = Field(default='Checking', index=True)

    def __str__(self):
        return f'{self.bank} - {self.name}'
    
    def __repr__(self):
        return f'Bank: {self.bank}; Account Type: {self.name}'
    
def db_get_accounts():
    with Session(appConfig.connection) as session:
        statement = select(Account).order_by(Account.created_at)
        results = session.exec(statement)
        return results.fetchall()

def db_add_account(bank: str, name: str):
    account = Account(bank=bank, name=name)
    account.create()
    return account