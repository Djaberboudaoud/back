from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.services import company as company_service
from app.schemas.company import CompanyCreate, CompanyUpdate, CompanyResponse

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get("/", response_model=List[CompanyResponse])
def get_all(db: Session = Depends(get_db)):
    return company_service.get_all(db)


@router.get("/{company_id}", response_model=CompanyResponse)
def get_by_id(company_id: int, db: Session = Depends(get_db)):
    company = company_service.get_by_id(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.post("/", response_model=CompanyResponse)
def create(data: CompanyCreate, db: Session = Depends(get_db)):
    return company_service.create(db, data)


@router.put("/{company_id}", response_model=CompanyResponse)
def update(company_id: int, data: CompanyUpdate, db: Session = Depends(get_db)):
    company = company_service.update(db, company_id, data)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.delete("/{company_id}")
def delete(company_id: int, db: Session = Depends(get_db)):
    if not company_service.delete(db, company_id):
        raise HTTPException(status_code=404, detail="Company not found")
    return {"message": "Company deleted"}
