from sqlalchemy.orm import Session
from app.models.location import Location
from app.schemas.location import LocationCreate, LocationUpdate


def get_all(db: Session):
    return db.query(Location).all()


def get_by_id(db: Session, location_id: int):
    return db.query(Location).filter(Location.id == location_id).first()


def create(db: Session, data: LocationCreate):
    location = Location(name=data.name)
    db.add(location)
    db.commit()
    db.refresh(location)
    return location


def update(db: Session, location_id: int, data: LocationUpdate):
    location = db.query(Location).filter(Location.id == location_id).first()
    if not location:
        return None
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(location, key, value)
    db.commit()
    db.refresh(location)
    return location


def delete(db: Session, location_id: int):
    location = db.query(Location).filter(Location.id == location_id).first()
    if not location:
        return False
    db.delete(location)
    db.commit()
    return True
