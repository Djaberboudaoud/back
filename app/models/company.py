from sqlalchemy import Column, Integer, String, DateTime, Enum as SAEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.session import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    type = Column(SAEnum("internal", "contractor", name="company_type"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    units = relationship("Unit", back_populates="company", cascade="all, delete-orphan")
    users = relationship("User", back_populates="company")
    cases = relationship("Case", back_populates="company")
