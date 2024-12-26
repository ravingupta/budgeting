from typing import Optional
from sqlmodel import Field

from .base import BaseModel

class Category(BaseModel, table=True):
    name: str = Field(index=True, unique=True)
    parent_id: Optional[int] = Field(default=None, foreign_key="category.id")
    description: Optional[str] = Field(default=None)
