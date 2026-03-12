from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database.session import get_db
from app.models.case import Case
from app.models.company import Company
from app.models.user import User
from app.models.notification import Notification

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total_cases = db.query(func.count(Case.id)).scalar()
    open_cases = db.query(func.count(Case.id)).filter(Case.status == "open").scalar()
    in_progress_cases = db.query(func.count(Case.id)).filter(Case.status == "in_progress").scalar()
    closed_cases = db.query(func.count(Case.id)).filter(Case.status == "closed").scalar()
    total_companies = db.query(func.count(Company.id)).scalar()
    total_users = db.query(func.count(User.id)).scalar()

    return {
        "total_cases": total_cases,
        "open_cases": open_cases,
        "in_progress_cases": in_progress_cases,
        "closed_cases": closed_cases,
        "total_companies": total_companies,
        "total_users": total_users,
    }
