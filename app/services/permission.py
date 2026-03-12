from sqlalchemy.orm import Session
from app.models.permission import Permission
from app.schemas.permission import PermissionCreate


def get_by_user(db: Session, user_id: int):
    return db.query(Permission).filter(Permission.user_id == user_id).all()


def create(db: Session, data: PermissionCreate):
    permission = Permission(user_id=data.user_id, permission_name=data.permission_name)
    db.add(permission)
    db.commit()
    db.refresh(permission)
    return permission


def delete(db: Session, permission_id: int):
    permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if not permission:
        return False
    db.delete(permission)
    db.commit()
    return True
