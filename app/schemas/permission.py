from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PermissionCreate(BaseModel):
    user_id: int
    permission_name: str


class PermissionResponse(BaseModel):
    id: int
    user_id: Optional[int] = None
    permission_name: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
