from pydantic import BaseModel


class BaseClient(BaseModel):
    name: str
    email: str
    phone: str


class CreateClientRequest(BaseClient):
    ...


class ClientResponse(BaseClient):
    id: int
