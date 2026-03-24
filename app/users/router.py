from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.users import service, schema
from app.auth.dependencies import get_current_user
from app.users.model import User

router = APIRouter()


# 🔹 Crear usuario
@router.post("/", response_model=schema.UserResponse)
def create_user(
    user_data: schema.UserCreate,
    db: Session = Depends(get_db)
):
    return service.create_user(db, user_data)


# 🔹 Listar usuarios (protegido)
@router.get("/", response_model=List[schema.UserResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return service.get_users(db)


# 🔹 Usuario actual
@router.get("/me", response_model=schema.UserResponse)
def read_me(
    current_user: User = Depends(get_current_user)
):
    return current_user


# 🔹 Obtener usuario por ID
@router.get("/{user_id}", response_model=schema.UserResponse)
def get_user_by_id(
    user_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = service.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user


# 🔹 Eliminar usuario
@router.delete("/{user_id}")
def delete_user(
    user_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = service.delete_user(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return {"message": "Usuario eliminado"}