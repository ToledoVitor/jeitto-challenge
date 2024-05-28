from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from ..src.database import Base
from ..src.main import app, get_db


# TEST DATABASE SETUP
SQLALCHEMY_DATABASE_URL = "sqlite:///./fast/tests/test_db.sqlite3"


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
        db.flush()


app.dependency_overrides[get_db] = mock_get_db

client = TestClient(app)


# APP TESTING
def test_create_client():
    # Arrange
    json = {
        "name": "José Teste",
        "email": "jose@gmail.com",
        "phone": "1199998888",
    }

    # Act
    response = client.post("/clients", json=json)

    # Assert
    assert response.status_code == 200

    json = response.json()
    assert json["name"] == "José Teste"
    assert json["email"] == "jose@gmail.com"
    assert json["phone"] == "1199998888"

    client_id = json["id"]
    client.delete(f"/clients/{client_id}")


def test_create_client_exists():
    # Arrange
    json = {
        "name": "Joao Teste",
        "email": "joao@gmail.com",
        "phone": "1199998888",
    }

    # Act
    response = client.post("/clients", json=json)
    assert response.status_code == 200
    client_id = response.json()["id"]

    response = client.post("/clients", json=json)

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Email já cadastrado"}

    client.delete(f"/clients/{client_id}")


def test_client_exists():
    # Arrange
    json = {
        "name": "Vitor Teste",
        "email": "vitor@gmail.com",
        "phone": "1199998888",
    }

    # Act
    create_res = client.post("/clients", json=json)
    assert create_res.status_code == 200

    client_id = create_res.json()["id"]
    error_res = client.get(f"/clients/{client_id}")

    # Assert
    assert error_res.status_code == 200

    json = error_res.json()
    assert json["name"] == "Vitor Teste"
    assert json["email"] == "vitor@gmail.com"
    assert json["phone"] == "1199998888"

    client.delete(f"/clients/{client_id}")


def test_client_dont_exists():
    response = client.get("/clients/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Cliente não encontrado"}
