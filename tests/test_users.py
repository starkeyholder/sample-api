"""
Example pytest test file for User Management API

This file contains ONE example test to get you started.
Your task is to add comprehensive test coverage for all endpoints.

pytest basics:
- Test functions must start with 'test_'
- Use assert statements for validation
- Use fixtures for setup/teardown
- Run with: pytest -v
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app, users_db
from datetime import datetime, timezone, UTC
# now = datetime.now(UTC)
client = TestClient(app)

# Fixture example - this runs before each test
@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_db():
    """Utility helper to reset DB before each test."""
    users_db.clear()
    now = datetime.now(timezone.utc)
    users_db["1"] = {
        "id": "1",
        "username": "andy",
        "email": "andy@gmail.com",
        "full_name": "Andy T.",
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }

    ##a second user db
    users_db["2"] = {
        "id": "2",
        "username": "mike",
        "email": "mike@atseng.com",
        "full_name": "Mike T.",
        "is_active": False,
        "created_at": now,
        "updated_at": now,
    }

    yield   # test runs here
    users_db.clear()  # cleanup

# Example test - THIS IS YOUR STARTING POINT
# ====== PATTERN =======
def test_health_check(client):
    """Test that the health check endpoint returns 200"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert "timestamp" in response.json()

def test_create_user_success(client):
    payload = {
        "id" : "user_id",
        "username": "newuser",
        "email": "newuser@example.com",
        "full_name": "New User"
    }

    response = client.post("/users", json=payload)
    assert response.status_code == 201

    data = response.json()

    assert data["username"] == "newuser"
    assert data["email"] == "newuser@example.com"
    assert data["full_name"] == "New User"
    assert data["is_active"] is True
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data

def test_create_user_duplicate_username(client):
    payload = {
        "username": "andy",
        "email": "andy@gmail.com",
        "full_name": "Andy T."
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 409
    assert "already exists" in response.json()["detail"]

def test_create_user_duplicate_email(client):
    payload = {
        "username": "andy",
        "email": "jack@gmail.com",  # duplicate email
        "full_name": "Andy T"
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 409
    assert "already exists" in response.json()["detail"]

def test_create_user_invalid_email(client):
    payload = {
        "username": "andy",
        "email": "andy@gmail.com",
        "full_name": "Andy T"
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 409
    assert "already exists" in response.json()["detail"]

def test_create_user_invalid_username_too_short(client):
    payload = {
        "username": "an",
        "email": "andy@gmail.com",
        "full_name": "Andy T"
    }

    response = client.post("/users", json=payload)
    assert response.status_code == 422

def test_list_users_empty(client):
    users_db.clear()

    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []

def test_list_users_with_data(client):
    response = client.get("/users", params={"active_only": "false"})
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2

    usernames = {u["username"] for u in data}
    assert usernames == {"andy", "mike"}

    andy = next(u for u in data if u["username"] == "andy")
    assert andy["email"] == "andy@gmail.com"
    assert andy["full_name"] == "Andy T."
    assert andy["is_active"] is True
    assert "id" in andy
    assert "created_at" in andy
    assert "updated_at" in andy

def test_list_users_active_only(client):
    response = client.get("/users")
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1

    user = data[0]
    assert user["username"] == "andy"
    assert user["is_active"] is True

def test_get_user_success(client):
    # endpoint as in main.py - line 87:
    # @app.get("/users/{user_id}", response_model=User)
    # async def get_user(user_id: str):
    response = client.get("/users/1")
    assert response.status_code == 200

    user = response.json()

    assert user["id"] == "1"
    assert user["username"] == "andy"
    assert user["email"] == "andy@gmail.com"
    assert user["full_name"] == "Andy T."
    assert user["is_active"] is True

def test_get_user_not_found(client):
    # endpoint as in main.py - line 87:
    # @app.get("/users/{user_id}", response_model=User)
    # async def get_user(user_id: str):
    response = client.get("/users/999")
    assert response.status_code == 404
    
    data = response.json()
    assert data["detail"] == "User with id '999' not found"

def test_update_user_success(client):
    # endpoint as in main.py - line 98:
    # @app.put("/users/{user_id}", response_model=User)
    # async def update_user(user_id: str, user_data: UserUpdate):
    update_payload = {
        "email": "andy.new@example.com",
        "full_name": "Andy Tseng",
    }

    response = client.put("/users/1", json=update_payload)
    assert response.status_code == 200

    data = response.json()

    assert data["id"] == "1"
    assert data["username"] == "andy"

    assert data["email"] == "andy.new@example.com"
    assert data["full_name"] == "Andy Tseng"
    assert data["is_active"] is True # test with active/inactive to show Failed
    assert "created_at" in data
    assert "updated_at" in data

def test_update_user_not_found(client):
    # endpoint as in main.py - line 98:
    # @app.put("/users/{user_id}", response_model=User)
    # async def update_user(user_id: str, user_data: UserUpdate):

    update_payload = {
        "email": "johndoe@gmail.com",
        "full_name": "John Doe",
        "is_active": False,
    }

    response = client.put("/users/999", json=update_payload)
    assert response.status_code == 404

    data = response.json()
    assert data["detail"] == "User with id '999' not found"

def test_update_user_email_conflict(client):
    # endpoint as in main.py - line 110:
    # if user_data.email and user_data.email != user["email"]:
    #     for uid, u in users_db.items():
    #         if uid != user_id and u["email"] == user_data.email:
    #             raise HTTPException(
    #                 status_code=status.HTTP_409_CONFLICT,
    #                 detail=f"Email '{user_data.email}' already exists"
    #             )

    update_payload = {
        "email": "andy@gmail.com",
        "full_name": "Mike T.",
    }

    response = client.put("/users/2", json=update_payload)
    assert response.status_code == 409

    data = response.json()
    assert data["detail"] == "Email 'andy@gmail.com' already exists"

def test_delete_user_soft_delete(client):
    # endpoint as in main.py - line 143:
    # @app.delete("/users/{user_id}/permanent", status_code=status.HTTP_204_NO_CONTENT)
    # async def permanently_delete_user(user_id: str):
    
    # user = users_db[user_id]
    # del users_db[user_id]
    # return {"deleted": user["username"]}

    response = client.delete("/users/1")
    assert response.status_code == 204

    get_after = client.get("/users/1")
    assert get_after.status_code == 200

    user = get_after.json()
    assert user["id"] == "1"
    assert user["is_active"] is False

    active_only = client.get("/users").json()
    usernames = {u["username"] for u in active_only}
    assert "andy" not in usernames

def test_delete_user_permanent(client):

    get_before = client.get("/users/2")
    assert get_before.status_code == 200

    response = client.delete("/users/2/permanent")
    assert response.status_code == 204

    get_after = client.get("/users/2")
    assert get_after.status_code == 404
    assert get_after.json()["detail"] == "User with id '2' not found"

def test_delete_user_not_found(client):
 
    response = client.delete("/users/999")
    assert response.status_code == 404

    data = response.json()
    assert data["detail"] == "User with id '999' not found"


# TODO: Add more tests below
# Suggested tests to implement:
#
# 1. test_create_user_success - Create a valid user
# 2. test_create_user_duplicate_username - Try to create user with existing username
# 3. test_create_user_duplicate_email - Try to create user with existing email
# 4. test_create_user_invalid_email - Test email validation
# 5. test_create_user_invalid_username_too_short - Test username length validation
# 6. test_list_users_empty - List users when database is empty
# 7. test_list_users_with_data - List users with multiple users
# 8. test_list_users_active_only - Test the active_only filter
# 9. test_get_user_success - Get a specific user by ID
# 10. test_get_user_not_found - Try to get non-existent user
# 11. test_update_user_success - Update user information
# 12. test_update_user_not_found - Try to update non-existent user
# 13. test_update_user_email_conflict - Try to update to existing email
# 14. test_delete_user_soft_delete - Test soft delete (is_active=False)
# 15. test_delete_user_permanent - Test permanent deletion
# 16. test_delete_user_not_found - Try to delete non-existent user
#
# BONUS challenges:
# - Use pytest.mark.parametrize for testing multiple inputs
# - Create custom fixtures for common test data
# - Test error messages match expected format
# - Test timestamp updates on user modifications
