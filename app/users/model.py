from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from uuid import uuid4

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    email= Column(String (255), unique=True, nullable=False)
    password_hash = Column(String (255), nullable=False)
    role_id = Column(String,ForeignKey("roles.id"), nullable=False)
    name = Column(String(50), unique=True, nullable=False)

    role = relationship("Role")