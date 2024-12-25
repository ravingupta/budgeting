from fastapi import APIRouter

router = APIRouter()

@router.get("/banks")
async def read_banks():
    return {"banks": "This is a list of banks"}
