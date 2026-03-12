from sqlalchemy.orm import Session
from app.models.case_type import CaseType
from app.schemas.case_type import CaseTypeCreate, CaseTypeUpdate


def get_all(db: Session):
    return db.query(CaseType).all()


def get_by_id(db: Session, type_id: int):
    return db.query(CaseType).filter(CaseType.id == type_id).first()


def get_by_category(db: Session, category_id: int):
    return db.query(CaseType).filter(CaseType.category_id == category_id).all()


def create(db: Session, data: CaseTypeCreate):
    case_type = CaseType(name=data.name, description=data.description, category_id=data.category_id)
    db.add(case_type)
    db.commit()
    db.refresh(case_type)
    return case_type


def update(db: Session, type_id: int, data: CaseTypeUpdate):
    case_type = db.query(CaseType).filter(CaseType.id == type_id).first()
    if not case_type:
        return None
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(case_type, key, value)
    db.commit()
    db.refresh(case_type)
    return case_type


def delete(db: Session, type_id: int):
    case_type = db.query(CaseType).filter(CaseType.id == type_id).first()
    if not case_type:
        return False
    db.delete(case_type)
    db.commit()
    return True
