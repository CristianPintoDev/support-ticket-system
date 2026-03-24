from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.ticket.router import router as ticket_router
from app.users.router import router as users_router
from app.core.database import engine, Base
from app.users.model import User
from app.ticket.model import Ticket, TicketStatus, TicketAssignmentHistory
from app.role.model import Role


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Support Ticket System",
    description="API en desarrollo para gestión de tickets de soporte",
    version="0.1.0",
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(ticket_router, prefix="/tickets", tags=["Tickets"])



def initdb():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    initdb()

