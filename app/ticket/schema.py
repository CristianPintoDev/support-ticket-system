from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class TicketBase(BaseModel):
    title: str
    description: str


class TicketCreate(TicketBase):
    create_by: str
    status_id: str


class TicketResponse(TicketBase):
    id: str
    create_by: str
    status_id: str
    create_at: datetime
    close_at: Optional[datetime]

    class Config:
        from_attributes = True

class TicketAssignmentHistoryResponse(BaseModel):
    id: str
    ticket_id: str
    assigned_to: str
    assigned_at: datetime

    class Config:
        from_attributes = True

class TicketAssignmentCreate(BaseModel):
    ticket_id: str
    assigned_to: str

class UpdateTicketStatus(TicketBase):
    status_id: str

    class Config:
        from_attributes = True

class TicketUpdate(TicketBase):
    status_id: Optional[int]
    closed: Optional[bool] = False

    class Config:
        from_attributes = True