from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.core.database import Base
from uuid import uuid4



class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    title = Column(String, nullable=False)
    description= Column(Text, nullable=False)
    create_by= Column(String, ForeignKey("users.id"), nullable=False)
    status_id= Column(String, ForeignKey("ticket_status.id"), nullable=False)
    create_at= Column(DateTime, default= lambda:datetime.now(timezone.utc), nullable=False)
    close_at= Column(DateTime, nullable=True)
    creator = relationship("User", back_populates="tickets")
    status= relationship("TicketStatus", back_populates="tickets")
    assignments = relationship("TicketAssignmentHistory", back_populates="ticket")


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, nullable=False)

    tickets = relationship("Ticket", back_populates="creator")

class TicketStatus(Base):
    __tablename__ = "ticket_status"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, unique=True, nullable=False)

    tickets = relationship("Ticket", back_populates="status")


class TicketAssignmentHistory(Base):
    __tablename__ = "ticket_assignment_history"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    ticket_id = Column(String, ForeignKey("tickets.id"), nullable=False)
    assigned_to = Column(String, ForeignKey("users.id"), nullable=False)
    assigned_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    ticket = relationship("Ticket", back_populates="assignments")

