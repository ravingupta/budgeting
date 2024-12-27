from fastapi import APIRouter, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from parsers import ScotiaParser

from models import db_get_accounts, db_get_transactions

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Account Transactions

@router.get("/{account_id}", response_class=HTMLResponse)
async def read_transactions(account_id: int, request: Request):
    account = db_get_accounts(account_id=account_id)
    transactions = db_get_transactions(account_id=account_id)
    output = {
        "request": request, 
        "account_id": account_id, 
        "account": account, 
        "transactions": transactions,
        "transactions_count": len(transactions)
    }
    return templates.TemplateResponse("transactions/index.html", output)

@router.post("/{account_id}")
async def add_transactions(account_id: int, file: UploadFile):
    account = db_get_accounts(account_id=account_id)
    if account.bank == "Scotia":
        await ScotiaParser(account_id=account_id, file=file.file).parse()
        return { "success": 1, "message": "File uploaded successfully" }
    return { "success": 0, "message": "Bank not supported" }
