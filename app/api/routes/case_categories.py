from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.services import case_category as category_service
from app.schemas.case_category import CaseCategoryCreate, CaseCategoryUpdate, CaseCategoryResponse

router = APIRouter(prefix="/case-categories", tags=["Case Categories"])


@router.get("/", response_model=List[CaseCategoryResponse])
def get_all(db: Session = Depends(get_db)):
    return category_service.get_all(db)


@router.get("/{category_id}", response_model=CaseCategoryResponse)
def get_by_id(category_id: int, db: Session = Depends(get_db)):
    category = category_service.get_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/", response_model=CaseCategoryResponse)
def create(data: CaseCategoryCreate, db: Session = Depends(get_db)):
    return category_service.create(db, data)


@router.put("/{category_id}", response_model=CaseCategoryResponse)
def update(category_id: int, data: CaseCategoryUpdate, db: Session = Depends(get_db)):
    category = category_service.update(db, category_id, data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete("/{category_id}")
def delete(category_id: int, db: Session = Depends(get_db)):
    if not category_service.delete(db, category_id):
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted"}
