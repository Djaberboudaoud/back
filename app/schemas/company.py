from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CompanyCreate(BaseModel):
    name: str
    type: str  # "internal" or "contractor"


class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None


class CompanyResponse(BaseModel):
    id: int
    name: str
    type: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
