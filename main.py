import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import appConfig
from app import accounts_router

from models import Category

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(accounts_router, prefix="/accounts", tags=["accounts"])

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=appConfig.DEBUG)
