from sqlalchemy import Column, Integer, String

from .database import Base


class Client(Base):
    __tablename__ = "client"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    email: str = Column(String, unique=True, index=True)
    phone: str = Column(String)
