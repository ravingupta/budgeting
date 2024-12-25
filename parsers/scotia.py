from parsers.parser import Parser

class ScotiaParser(Parser):
    def __init__(self, file):
        self.super().__init__(file)

    def parse(self):
        with open(self.file, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:
                parts = line.split(',')
                date = parts[1]
                description = parts[2]
                sub_description = parts[3]
                amount = parts[5]
                self.transactions.append({
                    'date': date,
                    'description': description + ' - ' + sub_description,
                    'amount': amount,
                    'type': 'debit' if float(amount) < 0 else 'credit'
                })
        return self.transactions
