from typing import Optional
from sqlmodel import Field, SQLModel, Session
from datetime import datetime

from config import appConfig

class BaseModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: str = Field(default=None)
    updated_at: str = Field(default=None)
    
    def create(self):
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        with Session(appConfig.connection) as session:
            session.add(self)
            session.commit()
    
    def update(self):
        self.updated_at = datetime.now().isoformat()
        with Session(appConfig.connection) as session:
            session.add(self)
            session.commit()