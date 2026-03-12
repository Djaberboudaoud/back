from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database.session import get_db
from app.services import case as case_service
from app.schemas.case import CaseCreate, CaseUpdate, CaseResponse

router = APIRouter(prefix="/cases", tags=["Cases"])


@router.get("/", response_model=List[CaseResponse])
def get_all(
    status: Optional[str] = Query(None),
    company_id: Optional[int] = Query(None),
    category_id: Optional[int] = Query(None),
    location_id: Optional[int] = Query(None),
    reported_by: Optional[int] = Query(None),
    send_to: Optional[int] = Query(None),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    return case_service.get_all(
        db,
        status=status,
        company_id=company_id,
        category_id=category_id,
        location_id=location_id,
        reported_by=reported_by,
        send_to=send_to,
        search=search,
    )


@router.get("/{case_id}", response_model=CaseResponse)
def get_by_id(case_id: int, db: Session = Depends(get_db)):
    case = case_service.get_by_id(db, case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return case


@router.post("/", response_model=CaseResponse)
def create(data: CaseCreate, db: Session = Depends(get_db)):
    return case_service.create(db, data)


@router.put("/{case_id}", response_model=CaseResponse)
def update(case_id: int, data: CaseUpdate, db: Session = Depends(get_db)):
    case = case_service.update(db, case_id, data)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return case


@router.delete("/{case_id}")
def delete(case_id: int, db: Session = Depends(get_db)):
    if not case_service.delete(db, case_id):
        raise HTTPException(status_code=404, detail="Case not found")
    return {"message": "Case deleted"}
