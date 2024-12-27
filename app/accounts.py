from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from constants.apis import ApiResponse
from models import db_get_accounts, db_add_account, db_get_transactions

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# All Accounts

@router.get("/", response_class=HTMLResponse)
async def read_accounts(request: Request):
    accounts = db_get_accounts()
    output = {"request": request, "accounts": accounts}
    return templates.TemplateResponse("accounts/index.html", output)

@router.post("/")
async def add_accounts(request: Request) -> ApiResponse:
    try:
        request_data = await request.json()
        db_add_account(request_data['bank'], request_data['name'])
        return {"success": 1, "message": "Account added successfully"}
    except Exception as e:
        return {"success": 0, "message": f"Error: {e}"}


# Single Account

@router.put("/{account_id}")
async def update_account(account_id: int, request: Request) -> ApiResponse:
    return {"message": f"Account {account_id} updated successfully"}

@router.get("/{account_id}", response_class=HTMLResponse)
async def read_account(account_id: int, request: Request):
    account = db_get_accounts(account_id=account_id)
    transactions = db_get_transactions(account_id=account_id)
    output = {
        "request": request, 
        "account_id": account_id, 
        "account": account, 
        "transactions": transactions,
        "transactions_count": len(transactions)
    }
    return templates.TemplateResponse("accounts/details.html", output)
