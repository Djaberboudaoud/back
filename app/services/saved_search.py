from sqlalchemy.orm import Session
from app.models.saved_search import SavedSearch
from app.schemas.saved_search import SavedSearchCreate


def get_by_user(db: Session, user_id: int):
    return db.query(SavedSearch).filter(SavedSearch.user_id == user_id).all()


def create(db: Session, data: SavedSearchCreate):
    saved = SavedSearch(user_id=data.user_id, case_id=data.case_id)
    db.add(saved)
    db.commit()
    db.refresh(saved)
    return saved


def delete(db: Session, saved_id: int):
    saved = db.query(SavedSearch).filter(SavedSearch.id == saved_id).first()
    if not saved:
        return False
    db.delete(saved)
    db.commit()
    return True
