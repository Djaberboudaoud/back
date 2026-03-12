from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.session import Base


class CaseCategory(Base):
    __tablename__ = "case_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    case_types = relationship("CaseType", back_populates="category", cascade="all, delete-orphan")
    cases = relationship("Case", back_populates="category")
