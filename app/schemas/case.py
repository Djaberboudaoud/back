from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date


class CaseCreate(BaseModel):
    title: str
    description: Optional[str] = None
    category_id: Optional[int] = None
    case_type_id: Optional[int] = None
    location_id: Optional[int] = None
    company_id: Optional[int] = None
    unit_id: Optional[int] = None
    reported_by: Optional[int] = None
    send_to: Optional[int] = None
    work_activity: Optional[str] = None
    system_involved: Optional[str] = None
    system_description: Optional[str] = None
    status: str = "open"
    equipment_involved: Optional[str] = None
    equipment_description: Optional[str] = None
    actual_consequences: Optional[str] = None
    potential_consequences: Optional[str] = None
    communication_causes: Optional[str] = None
    management_causes: Optional[str] = None
    training_causes: Optional[str] = None
    operating_environment_causes: Optional[str] = None
    equipment_causes: Optional[str] = None
    comments: Optional[str] = None
    due_date: Optional[date] = None


class CaseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    case_type_id: Optional[int] = None
    location_id: Optional[int] = None
    company_id: Optional[int] = None
    unit_id: Optional[int] = None
    reported_by: Optional[int] = None
    send_to: Optional[int] = None
    work_activity: Optional[str] = None
    system_involved: Optional[str] = None
    system_description: Optional[str] = None
    status: Optional[str] = None
    equipment_involved: Optional[str] = None
    equipment_description: Optional[str] = None
    actual_consequences: Optional[str] = None
    potential_consequences: Optional[str] = None
    communication_causes: Optional[str] = None
    management_causes: Optional[str] = None
    training_causes: Optional[str] = None
    operating_environment_causes: Optional[str] = None
    equipment_causes: Optional[str] = None
    comments: Optional[str] = None
    due_date: Optional[date] = None


class CaseResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    category_id: Optional[int] = None
    case_type_id: Optional[int] = None
    location_id: Optional[int] = None
    company_id: Optional[int] = None
    unit_id: Optional[int] = None
    reported_by: Optional[int] = None
    send_to: Optional[int] = None
    work_activity: Optional[str] = None
    system_involved: Optional[str] = None
    system_description: Optional[str] = None
    status: str
    equipment_involved: Optional[str] = None
    equipment_description: Optional[str] = None
    actual_consequences: Optional[str] = None
    potential_consequences: Optional[str] = None
    communication_causes: Optional[str] = None
    management_causes: Optional[str] = None
    training_causes: Optional[str] = None
    operating_environment_causes: Optional[str] = None
    equipment_causes: Optional[str] = None
    comments: Optional[str] = None
    due_date: Optional[date] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
