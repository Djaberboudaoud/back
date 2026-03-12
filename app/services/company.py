from sqlalchemy.orm import Session
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


def get_all(db: Session):
    return db.query(Company).all()


def get_by_id(db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()


def create(db: Session, data: CompanyCreate):
    company = Company(name=data.name, type=data.type)
    db.add(company)
    db.commit()
    db.refresh(company)
    return company


def update(db: Session, company_id: int, data: CompanyUpdate):
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        return None
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(company, key, value)
    db.commit()
    db.refresh(company)
    return company


def delete(db: Session, company_id: int):
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        return False
    db.delete(company)
    db.commit()
    return True
