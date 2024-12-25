from sqlmodel import SQLModel
from config import appConfig

from .account import Account
from .category import Category
from .transaction import Transaction

SQLModel.metadata.create_all(appConfig.connection)