from typing import Optional
from sqlmodel import Field

from .base import BaseModel

class Transaction(BaseModel, table=True):
    account_id: int = Field(foreign_key='account.id')
    date: str = Field()
    description: str = Field()
    amount: float = Field()
    type: Optional[str] = Field(default=None)
    category: Optional[str] = Field(default=None, index=True, foreign_key="category.id")
    tags: Optional[str] = Field(default=None)
    notes: Optional[str] = Field(default=None)

    def __str__(self):
        return f'{self.date} - {self.description} - {self.amount} - {self.type}'
    
    def __repr__(self):
        return f'{self.date} - {self.description} - {self.amount} - {self.type}'