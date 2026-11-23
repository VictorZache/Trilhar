import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend"))

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "app.db")
if os.path.exists(db_path):
    os.remove(db_path)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

r = client.get("/cadastro")
print("GET /cadastro:", r.status_code)

r = client.post("/cadastro", data={"username": "teste_direto", "email": "direto@teste.com", "senha": "123456", "confirmar_senha": "123456"})
print("POST /cadastro:", r.status_code)
print(r.text[:800])

r = client.post("/login", data={"username": "teste_direto", "senha": "123456"}, allow_redirects=False)
print("POST /login:", r.status_code, "cookies:", dict(r.cookies))
