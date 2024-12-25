from fastapi import FastAPI
import uvicorn

from config import appConfig
from app import banks_router

from models import Category

app = FastAPI()

app.include_router(banks_router, prefix="/banks")

# Test route
@app.get("/test")
def read_root():
    return {"Hello": "World"}

@app.get("/db")
def read_db():
    Category(name='Food & Dining').create()
    return {"DB_URI": appConfig.DB_URI}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=appConfig.DEBUG)
