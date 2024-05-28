from sqlalchemy import Column, Integer, String

from .database import Base


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
