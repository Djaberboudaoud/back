from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UnitCreate(BaseModel):
    name: str
    company_id: int


class UnitUpdate(BaseModel):
    name: Optional[str] = None
    company_id: Optional[int] = None


class UnitResponse(BaseModel):
    id: int
    name: str
    company_id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
