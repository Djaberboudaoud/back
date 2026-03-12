from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.services import notification as notification_service
from app.schemas.notification import NotificationCreate, NotificationResponse

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("/{user_id}", response_model=List[NotificationResponse])
def get_by_user(user_id: int, db: Session = Depends(get_db)):
    return notification_service.get_by_user(db, user_id)


@router.get("/{user_id}/unread-count")
def get_unread_count(user_id: int, db: Session = Depends(get_db)):
    count = notification_service.get_unread_count(db, user_id)
    return {"count": count}


@router.post("/", response_model=NotificationResponse)
def create(data: NotificationCreate, db: Session = Depends(get_db)):
    return notification_service.create(db, data)


@router.put("/{notification_id}/read", response_model=NotificationResponse)
def mark_as_read(notification_id: int, db: Session = Depends(get_db)):
    notification = notification_service.mark_as_read(db, notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification


@router.put("/{user_id}/read-all")
def mark_all_read(user_id: int, db: Session = Depends(get_db)):
    notification_service.mark_all_read(db, user_id)
    return {"message": "All notifications marked as read"}


@router.delete("/{notification_id}")
def delete(notification_id: int, db: Session = Depends(get_db)):
    if not notification_service.delete(db, notification_id):
        raise HTTPException(status_code=404, detail="Notification not found")
    return {"message": "Notification deleted"}
