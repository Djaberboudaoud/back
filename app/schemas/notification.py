from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NotificationCreate(BaseModel):
    user_id: int
    case_id: int


class NotificationResponse(BaseModel):
    id: int
    user_id: Optional[int] = None
    case_id: Optional[int] = None
    is_read: bool = False
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
