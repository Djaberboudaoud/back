from sqlalchemy.orm import Session
from app.models.case_category import CaseCategory
from app.schemas.case_category import CaseCategoryCreate, CaseCategoryUpdate


def get_all(db: Session):
    return db.query(CaseCategory).all()


def get_by_id(db: Session, category_id: int):
    return db.query(CaseCategory).filter(CaseCategory.id == category_id).first()


def create(db: Session, data: CaseCategoryCreate):
    category = CaseCategory(name=data.name, description=data.description)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def update(db: Session, category_id: int, data: CaseCategoryUpdate):
    category = db.query(CaseCategory).filter(CaseCategory.id == category_id).first()
    if not category:
        return None
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(category, key, value)
    db.commit()
    db.refresh(category)
    return category


def delete(db: Session, category_id: int):
    category = db.query(CaseCategory).filter(CaseCategory.id == category_id).first()
    if not category:
        return False
    db.delete(category)
    db.commit()
    return True
