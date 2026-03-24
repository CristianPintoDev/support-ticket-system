from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.auth import service, schema

router = APIRouter()

@router.post("/login", response_model=schema.TokenResponse)
def login(data: schema.LoginRequest, db: Session = Depends(get_db)):
    token = service.login_user(db, data.email, data.password)

    if not token:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    return {
        "access_token": token,
        "token_type": "bearer"
    }