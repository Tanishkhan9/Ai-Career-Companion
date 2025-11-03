from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    # Use a temporary email to avoid collisions
    payload = {"email": "testuser@example.com", "password": "secret123", "full_name": "Test User"}
    r = client.post("/api/v1/users/register", json=payload)
    # Accept either created (201) or 200 depending on implementation
    assert r.status_code in (200, 201)
    data = r.json()
    assert data.get("email") == payload["email"]

    # Login
    r2 = client.post("/api/v1/users/login", json={"email": payload["email"], "password": payload["password"]})
    assert r2.status_code == 200
    t = r2.json()
    assert "access_token" in t
