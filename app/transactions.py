from fastapi import APIRouter, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from parsers import ScotiaParser

from models import db_get_accounts, db_get_transactions

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Account Tractions

@router.get("/{account_id}", response_class=HTMLResponse)
async def read_transactions(account_id: int, request: Request):
    account = db_get_accounts(account_id=account_id)
    transactions = db_get_transactions(account_id=account_id)
    return templates.TemplateResponse("account.html", {"request": request, "account_id": account_id, "account": account, "transactions": transactions })

@router.post("/{account_id}")
async def read_transactions(account_id: int, file: UploadFile):
    # print("Uploaded file name", file.filename)
    # content = await file.read()
    await ScotiaParser(account_id=account_id, file=file.file).parse()
    return { "success": 1, "message": "File uploaded successfully" }
