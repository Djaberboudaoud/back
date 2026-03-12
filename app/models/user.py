from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    role = Column(SAEnum("basic", "extensive", "administrator", name="user_role"), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="RESTRICT"), nullable=False)
    unit_id = Column(Integer, ForeignKey("units.id", ondelete="RESTRICT"), nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    company = relationship("Company", back_populates="users")
    unit = relationship("Unit", back_populates="users")
    reported_cases = relationship("Case", foreign_keys="Case.reported_by", back_populates="reporter")
    assigned_cases = relationship("Case", foreign_keys="Case.send_to", back_populates="assignee")
    saved_searches = relationship("SavedSearch", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    permissions = relationship("Permission", back_populates="user", cascade="all, delete-orphan")
