from typing import Optional
from sqlmodel import Field, Session, select

from config import appConfig

from .base import BaseModel

class Category(BaseModel, table=True):
    name: str = Field(index=True, unique=True)
    parent_id: Optional[int] = Field(default=None, foreign_key="category.id")
    description: Optional[str] = Field(default=None)

def db_get_categories():
    with Session(appConfig.connection) as session:
        statement = select(Category)
        result = session.exec(statement)
        return result.fetchall()