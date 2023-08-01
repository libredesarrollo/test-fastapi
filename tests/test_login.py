import httpx
import pytest

# @pytest.mark.asyncio
# async def test_create_token(default_client: httpx.AsyncClient) -> None:
#     payload = {
#         "email": "admintest@admin.com",
#         "name": "andres",
#         "surname": "cruz",
#         "website": "https://www.desarrollolibre.net/",
#         "password": "12345",
#     }

#     headers = {
#         "accept": "application/json",
#         "Content-Type": "application/json"
#     }

#     response = await default_client.post("/register", json=payload, headers=headers)

#     assert response.status_code == 201
#     assert response.json() == {
#         "message": "User created successfully"
#     }

# @pytest.mark.asyncio
# async def test_create_token(default_client: httpx.AsyncClient) -> None:
#     payload = {
#         "username": "admintest@admin.com",
#         "password": "12345",
#     }


#     headers = {
#         "accept": "application/json",
#         # "Content-Type": "application/json"
#     }

#     response = await default_client.post("/token", data=payload, headers=headers)

#     assert response.status_code == 200
#     assert "access_token" in response.json()


# @pytest.mark.asyncio
# async def test_sign_user_in(default_client: httpx.AsyncClient) -> None:
#     payload = {
        # "email": "admintest@admin.com",
        # "hashed_password": "12345",
#     }

#     headers = {
#         "accept": "application/json",
#         "Content-Type": "application/x-www-form-urlencoded"
#     }

#     response = await default_client.post("/user/signin", data=payload, headers=headers)

#     assert response.status_code == 200
#     assert response.json()["token_type"] == "Bearer"



# @pytest.mark.asyncio
# async def test_create_task(default_client: httpx.AsyncClient) -> None:
#     payload = {
#         "name": 'task 1',
#         "description": 'description',
#         "status": 'done',
#         "category_id": 1,
#         "user_id": 13
#     }


#     headers = {
#         "accept": "application/json",
#         "Content-Type": "application/json"
#     }

#     response = await default_client.post("/tasks/add", json=payload, headers=headers)

#     assert response.status_code == 200
#     assert "access_token" in response.json()

from sqlalchemy.orm import Session

from database.database import get_database_session
from database.task import crud

@pytest.mark.asyncio
async def test_index_task(default_client: httpx.AsyncClient, db: Session =  next(get_database_session())) -> None:
 
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    tasks = crud.getAll(db)
    print(len(tasks))

    response = await default_client.get("/tasks/", headers=headers)

    assert response.status_code == 200
    assert len(response.json()["tasks"]) == len(tasks)