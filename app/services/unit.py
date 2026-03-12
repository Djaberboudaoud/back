from sqlalchemy.orm import Session
from app.models.unit import Unit
from app.schemas.unit import UnitCreate, UnitUpdate


def get_all(db: Session):
    return db.query(Unit).all()


def get_by_id(db: Session, unit_id: int):
    return db.query(Unit).filter(Unit.id == unit_id).first()


def get_by_company(db: Session, company_id: int):
    return db.query(Unit).filter(Unit.company_id == company_id).all()


def create(db: Session, data: UnitCreate):
    unit = Unit(name=data.name, company_id=data.company_id)
    db.add(unit)
    db.commit()
    db.refresh(unit)
    return unit


def update(db: Session, unit_id: int, data: UnitUpdate):
    unit = db.query(Unit).filter(Unit.id == unit_id).first()
    if not unit:
        return None
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(unit, key, value)
    db.commit()
    db.refresh(unit)
    return unit


def delete(db: Session, unit_id: int):
    unit = db.query(Unit).filter(Unit.id == unit_id).first()
    if not unit:
        return False
    db.delete(unit)
    db.commit()
    return True
