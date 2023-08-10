from fastapi.testclient import TestClient


from database.database import get_database_session
from api import app

# SQLALCHEMY_DATABASE_URL = "sqlite://"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False},
#     poolclass=StaticPool,
# )
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base.metadata.create_all(bind=engine)


# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()


app.dependency_overrides[get_database_session] = get_database_session

client = TestClient(app)

def test_create_user():

    payload = {
        "email": "admintest@admin.com",
        "name": "andres",
        "surname": "cruz",
        "website": "https://www.desarrollolibre.net/",
        "password": "12345",
    }

    response = client.post(
        "/register",
        json=payload,
    )

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "admintest@admin.com"
    assert "id" in data
    user_id = data["id"]

    # response = client.get(f"/users/{user_id}")
    # assert response.status_code == 200, response.text
    # data = response.json()
    # assert data["email"] == "deadpool@example.com"
    # assert data["id"] == user_id
def test_login_user():

    payload = {
        "username": "admintest@admin.com",
        "password": "12345",
    }

    response = client.post(
        "/token",
        data=payload,
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

    # response = client.get(f"/users/{user_id}")
    # assert response.status_code == 200, response.text
    # data = response.json()
    # assert data["email"] == "deadpool@example.com"
    # assert data["id"] == user_id
