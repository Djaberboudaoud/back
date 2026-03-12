from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database.session import get_db
from app.services import case_type as type_service
from app.schemas.case_type import CaseTypeCreate, CaseTypeUpdate, CaseTypeResponse

router = APIRouter(prefix="/case-types", tags=["Case Types"])


@router.get("/", response_model=List[CaseTypeResponse])
def get_all(category_id: Optional[int] = Query(None), db: Session = Depends(get_db)):
    if category_id:
        return type_service.get_by_category(db, category_id)
    return type_service.get_all(db)


@router.get("/{type_id}", response_model=CaseTypeResponse)
def get_by_id(type_id: int, db: Session = Depends(get_db)):
    case_type = type_service.get_by_id(db, type_id)
    if not case_type:
        raise HTTPException(status_code=404, detail="Case type not found")
    return case_type


@router.post("/", response_model=CaseTypeResponse)
def create(data: CaseTypeCreate, db: Session = Depends(get_db)):
    return type_service.create(db, data)


@router.put("/{type_id}", response_model=CaseTypeResponse)
def update(type_id: int, data: CaseTypeUpdate, db: Session = Depends(get_db)):
    case_type = type_service.update(db, type_id, data)
    if not case_type:
        raise HTTPException(status_code=404, detail="Case type not found")
    return case_type


@router.delete("/{type_id}")
def delete(type_id: int, db: Session = Depends(get_db)):
    if not type_service.delete(db, type_id):
        raise HTTPException(status_code=404, detail="Case type not found")
    return {"message": "Case type deleted"}
