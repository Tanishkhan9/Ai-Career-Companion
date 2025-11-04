from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)


def test_register_and_login():
	# Use a temporary email to avoid collisions
	payload = {"email": "testuser@example.com", "password": "secret123", "full_name": "Test User"}
	r = client.post("/api/v1/users/register", json=payload)
	# Accept either created (201) or 200 depending on implementation
	assert r.status_code in (200, 201)
	data = r.json()
	assert data.get("email") == payload["email"]

	# Try login; if forbidden due to unverified, perform verification
	r2 = client.post("/api/v1/users/login", json={"email": payload["email"], "password": payload["password"]})
	if r2.status_code == 403:
		user_id = data.get("id")
		if user_id:
			tmp_dir = os.path.join(os.path.dirname(__file__), "..", "tmp")
			token_path = os.path.abspath(os.path.join(tmp_dir, f"verification_{user_id}.token"))
			if os.path.exists(token_path):
				with open(token_path, "r") as f:
					token = f.read().strip()
				vr = client.post(f"/api/v1/users/verify?token={token}")
				assert vr.status_code in (200, 204)
		# retry login
		r2 = client.post("/api/v1/users/login", json={"email": payload["email"], "password": payload["password"]})

	assert r2.status_code == 200
	t = r2.json()
	assert "access_token" in t
