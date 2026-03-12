from sqlalchemy.orm import Session
from typing import Optional
from app.models.case import Case
from app.schemas.case import CaseCreate, CaseUpdate


def get_all(
    db: Session,
    status: Optional[str] = None,
    company_id: Optional[int] = None,
    category_id: Optional[int] = None,
    location_id: Optional[int] = None,
    reported_by: Optional[int] = None,
    send_to: Optional[int] = None,
    search: Optional[str] = None,
):
    query = db.query(Case)
    if status:
        query = query.filter(Case.status == status)
    if company_id:
        query = query.filter(Case.company_id == company_id)
    if category_id:
        query = query.filter(Case.category_id == category_id)
    if location_id:
        query = query.filter(Case.location_id == location_id)
    if reported_by:
        query = query.filter(Case.reported_by == reported_by)
    if send_to:
        query = query.filter(Case.send_to == send_to)
    if search:
        query = query.filter(Case.title.ilike(f"%{search}%"))
    return query.order_by(Case.created_at.desc()).all()


def get_by_id(db: Session, case_id: int):
    return db.query(Case).filter(Case.id == case_id).first()


def create(db: Session, data: CaseCreate):
    case = Case(**data.model_dump())
    db.add(case)
    db.commit()
    db.refresh(case)
    return case


def update(db: Session, case_id: int, data: CaseUpdate):
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        return None
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(case, key, value)
    db.commit()
    db.refresh(case)
    return case


def delete(db: Session, case_id: int):
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        return False
    db.delete(case)
    db.commit()
    return True
