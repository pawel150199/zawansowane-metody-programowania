from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.db import Base


class Report(Base):
    __tablename__ = "report"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    status = Column(String, index=True)
    content = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="report")
