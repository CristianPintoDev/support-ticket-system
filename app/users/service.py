from sqlalchemy.orm import Session
from app.users.model import User
from app.users.schema import UserCreate
from app.core.security import hash_password


# 🔹 Crear usuario
def create_user(db: Session, user_data: UserCreate):
    
    print("PASSWORD:", user_data.password)
    print("LEN:", len(user_data.password))
    
    
    # Verificar si el email ya existe
    existing_user = db.query(User).filter(User.email == user_data.email).first()

    if existing_user:
        raise ValueError("El email ya está registrado")

    # Crear usuario
    user = User(
        email=user_data.email,
        name=user_data.name,
        password_hash=hash_password(user_data.password),
        role_id=user_data.role_id
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# 🔹 Listar usuarios
def get_users(db: Session):
    return db.query(User).all()


# 🔹 Obtener usuario por ID
def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()


# 🔹 Obtener usuario por email (útil para auth)
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# 🔹 Eliminar usuario
def delete_user(db: Session, user_id: str):
    user = get_user_by_id(db, user_id)

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user