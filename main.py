import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import appConfig
from app import dashboard_router
from app import accounts_router
from app import trasactions_router


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


app.include_router(dashboard_router, tags=["dashboard"])
app.include_router(accounts_router, prefix="/accounts", tags=["accounts"])
app.include_router(trasactions_router, prefix="/transactions", tags=["transactions"])


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=appConfig.DEBUG)
