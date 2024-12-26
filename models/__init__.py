from sqlmodel import SQLModel
from config import appConfig

from .account import Account, db_get_accounts, db_add_account
from .category import Category
from .transaction import Transaction

SQLModel.metadata.create_all(appConfig.connection)