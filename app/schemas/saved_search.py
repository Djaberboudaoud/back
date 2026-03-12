from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SavedSearchCreate(BaseModel):
    user_id: int
    case_id: int


class SavedSearchResponse(BaseModel):
    id: int
    user_id: Optional[int] = None
    case_id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
