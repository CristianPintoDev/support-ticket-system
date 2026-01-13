from fastapi import FastAPI
from app.users.router import router as users_router
from app.auth.router import router as auth_router

app = FastAPI(
    title="Support Ticket System",
    description="API en desarrollo para gestión de tickets de soporte",
    version="0.1.0",
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(users_router, prefix="/users", tags=["Users"])


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Support Ticket System API (in development)"
    }
