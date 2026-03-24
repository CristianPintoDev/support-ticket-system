from pydantic import BaseModel, EmailStr


# 🔹 Base
class UserBase(BaseModel):
    email: EmailStr
    name: str
    role_id: str


# 🔹 Crear usuario
class UserCreate(UserBase):
    password: str


# 🔹 Respuesta
class UserResponse(UserBase):
    id: str

    class Config:
        from_attributes = True