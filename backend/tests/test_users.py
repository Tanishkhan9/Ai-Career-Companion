from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

import uuid

def test_register_and_login():
    # generate a unique email to avoid collisions on disk-based sqlite
    email = f"testuser+{uuid.uuid4().hex}@example.com"
    payload = {"email": email, "password": "secret123", "full_name": "Test User"}
    r = client.post("/api/v1/users/register", json=payload)
    # Accept created/ok or, if the address somehow already exists, the explicit 400
    if r.status_code == 400:
        assert r.json().get("detail") == "Email already registered"
    else:
        assert r.status_code in (200, 201)
        data = r.json()
        assert data.get("email") == payload["email"]

    # Login should work regardless (existing or just-created user)
    r2 = client.post("/api/v1/users/login", json={"email": payload["email"], "password": payload["password"]})
    assert r2.status_code == 200
    t = r2.json()
    assert "access_token" in t
