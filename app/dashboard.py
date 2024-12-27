from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models import db_get_accounts, db_get_categories

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    accounts = db_get_accounts()
    categories = db_get_categories()
    output = {
        "request": request, 
        "accounts": accounts, 
        "categories": categories
    }
    return templates.TemplateResponse("dashboard.html", output)