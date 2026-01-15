from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from app.core.database import Base

class TicketStatus(Base):
    __tablename__ = "ticket_status"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
