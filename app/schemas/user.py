from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: str
    role: str  # "basic", "extensive", "administrator"
    company_id: int
    unit_id: int
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
    company_id: Optional[int] = None
    unit_id: Optional[int] = None
    password: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    company_id: int
    unit_id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
