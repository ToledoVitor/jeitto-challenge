from sqlalchemy.orm import Session

from . import models, schemas


class ClientRepository:
    @staticmethod
    def get_client_by_id(db: Session, client_id: int) -> models.Client:
        return db.query(models.Client).filter(models.Client.id == client_id).first()

    @staticmethod
    def get_client_by_email(db: Session, email: str) -> models.Client:
        return db.query(models.Client).filter(models.Client.email == email).first()

    @staticmethod
    def create_client(
        db: Session, client: schemas.CreateClientRequest
    ) -> models.Client:
        db_client = models.Client(
            name=client.name,
            email=client.email,
            phone=client.phone,
        )

        db.add(db_client)
        db.commit()
        db.refresh(db_client)

        return db_client

    @staticmethod
    def delete_client(db: Session, client_id: int) -> None:
        db.query(models.Client).filter(models.Client.id == client_id).delete()
        db.commit()
