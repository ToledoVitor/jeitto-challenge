from pydantic import BaseModel


class CreateClient(BaseModel):
    name: str
    email: str
    phone: str


class Client(BaseModel):
    id: int
    name: str
    email: str
    phone: str
