from sqlalchemy.orm import Session

from . import models, schemas


def get_client_by_id(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def get_client_by_email(db: Session, email: str):
    return db.query(models.Client).filter(models.Client.email == email).first()


def create_client(db: Session, client: schemas.CreateClient):
    db_client = models.Client(
        name=client.name,
        email=client.email,
        phone=client.phone,
    )

    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client
