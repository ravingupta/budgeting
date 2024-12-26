import pandas as pd
from parsers.parser import Parser

class ScotiaParser(Parser):
    def __init__(self, account_id, file):
        super().__init__(account_id, file)

    async def parse(self):
        data = pd.read_csv(self.file, skiprows=1)
        data['description'] = data.iloc[:, 2] + ' - ' + data.iloc[:, 3]
        transactions = data.apply(lambda row: {
            'date': row[1],
            'description': row['description'],
            'amount': row[5],
            'type': 'debit' if row[5] < 0 else 'credit'
        }, axis=1).tolist()
        self.transactions.extend(transactions)
        await self.save_transactions()
