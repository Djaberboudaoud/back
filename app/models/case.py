from sqlalchemy import Column, Integer, String, Text, DateTime, Date, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.session import Base


class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    category_id = Column(Integer, ForeignKey("case_categories.id", ondelete="SET NULL"), nullable=True)
    case_type_id = Column(Integer, ForeignKey("case_types.id", ondelete="SET NULL"), nullable=True)

    location_id = Column(Integer, ForeignKey("locations.id", ondelete="SET NULL"), nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="SET NULL"), nullable=True)
    unit_id = Column(Integer, ForeignKey("units.id", ondelete="SET NULL"), nullable=True)

    reported_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    send_to = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    work_activity = Column(Text, nullable=True)
    system_involved = Column(Text, nullable=True)
    system_description = Column(Text, nullable=True)

    status = Column(
        SAEnum("open", "closed", "in_progress", name="case_status"),
        nullable=False,
        server_default="open"
    )

    equipment_involved = Column(Text, nullable=True)
    equipment_description = Column(Text, nullable=True)

    actual_consequences = Column(Text, nullable=True)
    potential_consequences = Column(Text, nullable=True)

    communication_causes = Column(Text, nullable=True)
    management_causes = Column(Text, nullable=True)
    training_causes = Column(Text, nullable=True)
    operating_environment_causes = Column(Text, nullable=True)
    equipment_causes = Column(Text, nullable=True)

    comments = Column(Text, nullable=True)

    due_date = Column(Date, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    category = relationship("CaseCategory", back_populates="cases")
    case_type = relationship("CaseType", back_populates="cases")
    location = relationship("Location", back_populates="cases")
    company = relationship("Company", back_populates="cases")
    unit = relationship("Unit", back_populates="cases")
    reporter = relationship("User", foreign_keys=[reported_by], back_populates="reported_cases")
    assignee = relationship("User", foreign_keys=[send_to], back_populates="assigned_cases")
    saved_searches = relationship("SavedSearch", back_populates="case", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="case", cascade="all, delete-orphan")
