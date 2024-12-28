from sqlmodel import SQLModel
from config import appConfig

from .account import Account, db_get_accounts, db_add_account
from .category import Category, db_get_categories
from .transaction import Transaction, db_get_transactions, db_add_transaction, db_get_transaction, db_update_transaction, db_transaction_summary

SQLModel.metadata.create_all(appConfig.connection)