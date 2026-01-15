from fastapi import FastAPI
from app.users.router import router as users_router
from app.auth.router import router as auth_router
from app.core.database import engine, Base


app = FastAPI(
    title="Support Ticket System",
    description="API en desarrollo para gestión de tickets de soporte",
    version="0.1.0",
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(users_router, prefix="/users", tags=["Users"])

def initdb():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    initdb()

