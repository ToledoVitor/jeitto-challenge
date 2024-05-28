from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from src.database import Base
from src.main import app, get_db
from src.models import Client


# TEST DATABASE SETUP
SQLALCHEMY_DATABASE_URL = "sqlite:///./fast/tests/test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base.metadata.create_all(bind=engine)


def mock_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.query(Client).delete()
        db.close()


app.dependency_overrides[get_db] = mock_get_db

client = TestClient(app)


# APP TESTING
def test_create_client():
    response = client.post(
        "/clients",
        json={
            "name": "José Teste",
            "email": "jose@gmail.com",
            "phone": "1199998888",
        },
    )
    assert response.status_code == 200

    json = response.json()
    assert json["name"] == "José Teste"
    assert json["email"] == "jose@gmail.com"
    assert json["phone"] == "1199998888"


def test_create_client_exists():
    response = client.post(
        "/clients",
        json={
            "name": "Joao Teste",
            "email": "joao@gmail.com",
            "phone": "1199998888",
        },
    )
    assert response.status_code == 200

    response = client.post(
        "/clients",
        json={
            "name": "Joao Teste",
            "email": "joao@gmail.com",
            "phone": "1199998888",
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Email já cadastrado"}


def test_client_exists():
    res = client.post(
        "/clients",
        json={
            "name": "Vitor Teste",
            "email": "vitor@gmail.com",
            "phone": "1199998888",
        },
    )
    assert res.status_code == 200

    client_id = res.json()["id"]
    response = client.get(f"/clients/{client_id}")

    assert response.status_code == 200

    json = response.json()
    assert json["name"] == "Vitor Teste"
    assert json["email"] == "vitor@gmail.com"
    assert json["phone"] == "1199998888"


def test_client_dont_exists():
    response = client.get("/clients/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Cliente não encontrado"}
