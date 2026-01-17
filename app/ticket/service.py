from sqlalchemy.orm import Session
from datetime import datetime, timezone
from uuid import UUID
from app.ticket.model import Ticket
from app.ticket.schema import TicketUpdate


def create_ticket(db, ticket_data):
    from app.ticket.model import Ticket
    from datetime import datetime, timezone

    ticket = Ticket(
        title=ticket_data.title,
        description=ticket_data.description,
        create_by=ticket_data.create_by,
        status_id=ticket_data.status_id,
        create_at=datetime.now(timezone.utc)
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def update_ticket(db: Session, ticket_id: UUID, data: TicketUpdate):
    ticket = get_ticket_by_id(db, ticket_id)
    if not ticket:
        return None

    if data.title is not None:
        ticket.title = data.title

    if data.description is not None:
        ticket.description = data.description

    if data.status_id is not None:
        ticket.status_id = data.status_id

    # Si se cierra el ticket
    if data.closed and ticket.closed_at is None:
        ticket.closed_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(ticket)
    return ticket

def close_ticket(db: Session, ticket_id: UUID, closed_status_id: str):
    ticket = get_ticket_by_id(db, ticket_id)
    if not ticket:
        return None

    ticket.status_id = closed_status_id  # Debes pasar el ID de estado "cerrado"
    ticket.closed_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(ticket)
    return ticket