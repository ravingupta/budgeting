from typing import List, Dict, Any, Optional
from pydantic import BaseModel

from models import db_add_transaction

class Parser(BaseModel):
    file: Any
    transactions: Optional[List[Dict[str, Any]]] = []
    account_id: int

    def __init__(self, account_id: int, file: Any):
        super().__init__(account_id=account_id, file=file)
        self.file = file
        self.transactions = []

    async def save_transactions(self):
        for t in self.transactions:
            try:
                db_add_transaction(account_id=self.account_id, **t)
            except Exception as e:
                print("Transaction Fail: ", str(e))