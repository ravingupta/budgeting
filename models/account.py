from typing import Optional, Union
from sqlmodel import Field

from .base import BaseModel

class Account(BaseModel, table=True):
    bank: str = Field(default=None, index=True)
    name: str = Field(default='Checking', index=True)

    def __str__(self):
        return f'{self.bank} - {self.name}'
    
    def __repr__(self):
        return f'Bank: {self.bank}; Account Type: {self.name}'