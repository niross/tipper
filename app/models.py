import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String, Text

from app.database import Base


class TipReport(Base):
    __tablename__ = "tip_reports"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    latitude = Column(Numeric, index=True)
    longitude = Column(Numeric, index=True)
    number_of_items = Column(Integer)
    description = Column(Text, nullable=True)
    is_hazardous = Column(Boolean, nullable=True)
    image = Column(String, nullable=True)
    reported = Column(DateTime, default=datetime.now())
    reporter_title = Column(String, nullable=True)
    reporter_first_name = Column(String, nullable=True)
    reporter_last_name = Column(String, nullable=True)
    reporter_email = Column(String, nullable=True)
    reporter_phone = Column(String, nullable=True)
