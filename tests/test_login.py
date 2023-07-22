import httpx
import pytest

@pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email": "admintest@admin.com",
        "name": "andres",
        "surname": "cruz",
        "website": "https://www.desarrollolibre.net/",
        "password": "12345",
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    response = await default_client.post("/register", json=payload, headers=headers)

    assert response.status_code == 201
    assert response.json() == {
        "message": "User created successfully"
    }


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