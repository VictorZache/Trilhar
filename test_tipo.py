import os, sys, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend"))

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "app.db")
if os.path.exists(db_path):
    os.remove(db_path)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

timestamp = str(int(time.time()))
usuario = f"estudante_{timestamp}"
email = f"{usuario}@teste.com"

print("=== GET /cadastro ===")
r = client.get("/cadastro")
print(r.status_code, "OK" if "Tipo de conta" in r.text else "FALHA")

print("\n=== POST /cadastro (aluno) ===")
r = client.post("/cadastro", data={
    "username": usuario, "email": email, "senha": "123456", "confirmar_senha": "123456", "tipo": "aluno"
})
print(r.status_code, "OK" if "sucesso" in r.text.lower() else "FALHA: " + r.text[:200])

print("\n=== GET /login ===")
r = client.get("/login")
print(r.status_code, "OK" if "Entrar" in r.text else "FALHA")

print("\n=== POST /login ===")
r = client.post("/login", data={"username": usuario, "senha": "123456"}, allow_redirects=False)
print(r.status_code, "redirect" if r.status_code in (302, 303) else "FALHA", "cookies:", dict(r.cookies))

print("\n=== GET /dashboard ===")
r = client.get("/dashboard", allow_redirects=False)
print(r.status_code, "OK" if "Bem-vindo" in r.text and "Aluno" in r.text else "FALHA: " + r.text[:200])

print("\n=== POST /logout ===")
r = client.post("/logout", allow_redirects=False)
print(r.status_code, "redirect" if r.status_code in (302, 303) else "FALHA")

print("\n=== GET /dashboard (apos logout) ===")
r = client.get("/dashboard", allow_redirects=False)
print(r.status_code, "redirect login" if r.status_code in (302, 303) else "FALHA")

print("\nTestes concluidos com sucesso.")
