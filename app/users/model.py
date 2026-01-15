from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email= Column(String (255), unique=True, nullable=False)
    password_hash = Column(String (255), nullable=False)
    role_id = Column(Integer,ForeignKey("roles.id"), nullable=False)
    name = Column(String(50), unique=True, nullable=False)

    role = relationship("Role")