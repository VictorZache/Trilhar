import os
import sys

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "app.db")
if os.path.exists(db_path):
    os.remove(db_path)

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend"))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

r = client.get("/cadastro")
print("GET /cadastro:", r.status_code, "OK" if "Criar conta" in r.text else "FALHA")

r = client.post("/cadastro", data={"username": "aluno", "email": "aluno@teste.com", "senha": "123456", "confirmar_senha": "123456"})
print("POST /cadastro:", r.status_code, "OK" if "Conta criada" in r.text else "FALHA: " + r.text[:300])

r = client.get("/login")
print("GET /login:", r.status_code, "OK" if "Entrar" in r.text else "FALHA")

r = client.post("/login", data={"username": "aluno", "senha": "errada"})
print("POST /login (senha errada):", r.status_code, "OK - 401" if r.status_code == 401 else "FALHA")

r = client.post("/login", data={"username": "aluno", "senha": "123456"}, allow_redirects=False)
print("POST /login (ok):", r.status_code, "redirect" if r.status_code in (302, 303) else "FALHA", "cookies:", dict(r.cookies))

r = client.get("/dashboard", allow_redirects=False)
print("GET /dashboard:", r.status_code, "OK" if "Bem-vindo" in r.text else "FALHA: " + r.text[:200])

r = client.post("/logout", allow_redirects=False)
print("POST /logout:", r.status_code, "redirect" if r.status_code in (302, 303) else "FALHA")

r = client.get("/dashboard", allow_redirects=False)
print("GET /dashboard (apos logout):", r.status_code, "redirect login" if r.status_code in (302, 303) else "FALHA: " + str(r.status_code))

print("\nTestes concluidos.")
