from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CaseTypeCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category_id: int


class CaseTypeUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None


class CaseTypeResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    category_id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
