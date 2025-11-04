from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

payload = {"email": "testuser@example.com", "password": "secret123", "full_name": "Test User"}
print('POST /api/v1/users/register')
r = client.post('/api/v1/users/register', json=payload)
print('status', r.status_code)
try:
    print('json', r.json())
except Exception as e:
    print('raw', r.text)

print('\nPOST /api/v1/users/login')
r2 = client.post('/api/v1/users/login', json={"email": payload['email'], "password": payload['password']})
print('status', r2.status_code)
try:
    print('json', r2.json())
except Exception as e:
    print('raw', r2.text)
