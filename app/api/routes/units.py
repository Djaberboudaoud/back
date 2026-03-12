from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database.session import get_db
from app.services import unit as unit_service
from app.schemas.unit import UnitCreate, UnitUpdate, UnitResponse

router = APIRouter(prefix="/units", tags=["Units"])


@router.get("/", response_model=List[UnitResponse])
def get_all(company_id: Optional[int] = Query(None), db: Session = Depends(get_db)):
    if company_id:
        return unit_service.get_by_company(db, company_id)
    return unit_service.get_all(db)


@router.get("/{unit_id}", response_model=UnitResponse)
def get_by_id(unit_id: int, db: Session = Depends(get_db)):
    unit = unit_service.get_by_id(db, unit_id)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit


@router.post("/", response_model=UnitResponse)
def create(data: UnitCreate, db: Session = Depends(get_db)):
    return unit_service.create(db, data)


@router.put("/{unit_id}", response_model=UnitResponse)
def update(unit_id: int, data: UnitUpdate, db: Session = Depends(get_db)):
    unit = unit_service.update(db, unit_id, data)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit


@router.delete("/{unit_id}")
def delete(unit_id: int, db: Session = Depends(get_db)):
    if not unit_service.delete(db, unit_id):
        raise HTTPException(status_code=404, detail="Unit not found")
    return {"message": "Unit deleted"}
