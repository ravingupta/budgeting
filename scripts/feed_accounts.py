from models import Account

def update_accounts() -> bool:
    try:
        Account(bank="Scotia", name="Chequing").create()
        Account(bank="Scotia", name="Savings").create()
        Account(bank="TD", name="Chequing").create()
        Account(bank="TD", name="Savings").create()
        return True
    except Exception as e:
        print(e)
    return False
