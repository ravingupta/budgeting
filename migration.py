from config import appConfig

from scripts.feed_categories import update_categories
from scripts.feed_accounts import update_accounts

def migrate_categories():
    if update_categories():
        print('Categories updated successfully.')
    else:
        print('Categories failed to update.')

def migrate_accounts():
    if update_accounts():
        print('Accounts updated successfully.')
    else:
        print('Accounts failed to update.')

if __name__ == '__main__':
    migrate_categories()
    migrate_accounts()
