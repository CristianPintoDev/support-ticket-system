from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_user
from app.users.model import User
from app.core.database import get_db
from app.ticket import service, schema


router = APIRouter()


@router.post("/", response_model=schema.TicketResponse)
def create_ticket(
    ticket_data: schema.TicketCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return service.create_ticket(db, ticket_data)

@router.get("/", response_model=list[schema.TicketResponse])
def list_tickets(db: Session = Depends(get_db)):
    return service.get_tickets(db)

@router.get("/{ticket_id}", response_model=schema.TicketResponse)
def get_ticket(ticket_id: str, db: Session = Depends(get_db)):
    return service.get_ticket(db, ticket_id)

@router.patch("/{ticket_id}/status", response_model=schema.TicketResponse)
def update_ticket_status(
    ticket_id: str,
    status_data: schema.UpdateTicketStatus,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
    ):
    return service.update_ticket_status(db, ticket_id, status_data)


@router.post("/{ticket_id}/assign")
def assign_ticket(
    ticket_id: str,
    data: schema.AssignTicket,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ticket = service.assign_ticket(db, ticket_id, data.assigned_to)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket o usuario no encontrado")

    return {"message": "Ticket asignado correctamente"}