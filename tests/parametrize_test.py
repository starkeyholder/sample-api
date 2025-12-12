# content of test_expectation.py
import pytest
from fastapi.testclient import TestClient
from app.main import app, users_db ## change py. to app.
from datetime import datetime, timezone, UTC

# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected

client = TestClient(app)
# Fixture example - this runs before each test
@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)

@pytest.fixture
def client():
    """Shared TestClient for the FastAPI app."""
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_db():
    """Seed users_db before each test and clean up after."""
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

    users_db["2"] = {
        "id": "2",
        "username": "mike",
        "email": "mike@atseng.com",
        "full_name": "Mike T.",
        "is_active": False,
        "created_at": now,
        "updated_at": now,
    }

    yield
    users_db.clear()

@pytest.mark.parametrize(
    "active_only,expected_usernames",
    [
        (True,  {"andy"}),
        (False, {"andy", "mike"})
    ]
)
def test_list_users_param(client, active_only, expected_usernames):
    response = client.get("/users", params={"active_only": active_only})
    assert response.status_code == 200

    data = response.json()
    usernames = {u["username"] for u in data}

    assert usernames == expected_usernames
