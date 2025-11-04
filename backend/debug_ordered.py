from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

print('GET /health')
print(client.get('/health').status_code, client.get('/health').json())

payload = {"email": "testuser@example.com", "password": "secret123", "full_name": "Test User"}
print('POST /api/v1/users/register')
r = client.post('/api/v1/users/register', json=payload)
print('status', r.status_code)
print('json', r.json())

print('POST /api/v1/users/register again (should fail)')
r2 = client.post('/api/v1/users/register', json=payload)
print('status', r2.status_code)
print('json', r2.json())
