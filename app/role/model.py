from sqlalchemy import Column, String
from app.core.database import Base
from uuid import uuid4


class Role(Base):
    __tablename__ = "roles"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(50), unique=True, nullable=False)