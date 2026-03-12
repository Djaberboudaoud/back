from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.services import permission as permission_service
from app.schemas.permission import PermissionCreate, PermissionResponse

router = APIRouter(prefix="/permissions", tags=["Permissions"])


@router.get("/{user_id}", response_model=List[PermissionResponse])
def get_by_user(user_id: int, db: Session = Depends(get_db)):
    return permission_service.get_by_user(db, user_id)


@router.post("/", response_model=PermissionResponse)
def create(data: PermissionCreate, db: Session = Depends(get_db)):
    return permission_service.create(db, data)


@router.delete("/{permission_id}")
def delete(permission_id: int, db: Session = Depends(get_db)):
    if not permission_service.delete(db, permission_id):
        raise HTTPException(status_code=404, detail="Permission not found")
    return {"message": "Permission deleted"}
