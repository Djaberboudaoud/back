from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CaseCategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None


class CaseCategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class CaseCategoryResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
