from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.services import saved_search as saved_service
from app.schemas.saved_search import SavedSearchCreate, SavedSearchResponse

router = APIRouter(prefix="/saved-searches", tags=["Saved Searches"])


@router.get("/{user_id}", response_model=List[SavedSearchResponse])
def get_by_user(user_id: int, db: Session = Depends(get_db)):
    return saved_service.get_by_user(db, user_id)


@router.post("/", response_model=SavedSearchResponse)
def create(data: SavedSearchCreate, db: Session = Depends(get_db)):
    return saved_service.create(db, data)


@router.delete("/{saved_id}")
def delete(saved_id: int, db: Session = Depends(get_db)):
    if not saved_service.delete(db, saved_id):
        raise HTTPException(status_code=404, detail="Saved search not found")
    return {"message": "Saved search deleted"}
