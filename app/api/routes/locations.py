from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.services import location as location_service
from app.schemas.location import LocationCreate, LocationUpdate, LocationResponse

router = APIRouter(prefix="/locations", tags=["Locations"])


@router.get("/", response_model=List[LocationResponse])
def get_all(db: Session = Depends(get_db)):
    return location_service.get_all(db)


@router.get("/{location_id}", response_model=LocationResponse)
def get_by_id(location_id: int, db: Session = Depends(get_db)):
    location = location_service.get_by_id(db, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location


@router.post("/", response_model=LocationResponse)
def create(data: LocationCreate, db: Session = Depends(get_db)):
    return location_service.create(db, data)


@router.put("/{location_id}", response_model=LocationResponse)
def update(location_id: int, data: LocationUpdate, db: Session = Depends(get_db)):
    location = location_service.update(db, location_id, data)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location


@router.delete("/{location_id}")
def delete(location_id: int, db: Session = Depends(get_db)):
    if not location_service.delete(db, location_id):
        raise HTTPException(status_code=404, detail="Location not found")
    return {"message": "Location deleted"}
