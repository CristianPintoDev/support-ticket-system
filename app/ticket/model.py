from sqlalchemy import Column, Integer, String, Text, DateTime,create_engine, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.core.database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    description= Column(Text, nullable=False)
    create_by= Column(Integer, ForeignKey("users,id"), nullable=False)
    status_id= Column(Integer, ForeignKey("status.id"), nullable=False)
    create_at= Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    close_at= Column(DateTime,default=datetime.now(timezone.utc), nullable=True)
    creator= relationship("User")
    status= relationship("Ticket_status")