from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
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


@app.get("/clients/{client_id}", response_model=schemas.Client)
def get_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_client_by_id(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return db_client


@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.CreateClient, db: Session = Depends(get_db)):
    db_client = crud.get_client_by_email(db, email=client.email)
    if db_client:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    return crud.create_client(db=db, client=client)
