from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)


def test_upload_resume_with_auth():
	# Register
	rr = client.post("/api/v1/users/register", json={"email": "resume_test@example.com", "password": "secret123", "full_name": "Resume Test"})
	assert rr.status_code in (200, 201)
	user = rr.json()

	# Try login; if forbidden, verify then retry
	login = client.post("/api/v1/users/login", json={"email": user["email"], "password": "secret123"})
	if login.status_code == 403:
		user_id = user.get("id")
		if user_id:
			tmp_dir = os.path.join(os.path.dirname(__file__), "..", "tmp")
			token_path = os.path.abspath(os.path.join(tmp_dir, f"verification_{user_id}.token"))
			if os.path.exists(token_path):
				with open(token_path, "r") as f:
					token = f.read().strip()
				vr = client.post(f"/api/v1/users/verify?token={token}")
				assert vr.status_code in (200, 204)
		login = client.post("/api/v1/users/login", json={"email": user["email"], "password": "secret123"})

	assert login.status_code == 200
	token = login.json()["access_token"]

	files = {"file": ("resume.txt", b"Python React FastAPI", "text/plain")}
	r = client.post("/api/v1/resume/upload", files=files, headers={"Authorization": f"Bearer {token}"})
	assert r.status_code == 200
	data = r.json()
	assert data["filename"] == "resume.txt"
	assert isinstance(data.get("skills"), list)
	assert "Python" in data.get("skills", [])


