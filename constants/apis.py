from fastapi.responses import Response
from pydantic import BaseModel
from typing import Optional

class ApiResponse(Response):
    success: int
    message: str = None
    data: Optional[dict] = None