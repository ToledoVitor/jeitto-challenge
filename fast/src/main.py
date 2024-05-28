from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .repository import ClientRepository
from .schemas import ClientResponse, CreateClientRequest

from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/clients/{client_id}", response_model=ClientResponse)
def get_client(client_id: int, db: Session = Depends(get_db)):
    db_client = ClientRepository.get_client_by_id(db=db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return db_client


@app.post("/clients/", response_model=ClientResponse)
def create_client(client: CreateClientRequest, db: Session = Depends(get_db)):
    db_client = ClientRepository.get_client_by_email(db, email=client.email)
    if db_client:
        raise HTTPException(status_code=400, detail="Email ja cadastrado")

    return ClientRepository.create_client(db=db, client=client)


@app.delete("/clients/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    return ClientRepository.delete_client(db=db, client_id=client_id)
