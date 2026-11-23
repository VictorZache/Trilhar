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

print("\n=== POST /cadastro (aluno) -> deve redirecionar para /aluno/quiz ===")
r = client.post("/cadastro", data={
    "username": usuario, "email": email, "senha": "123456", "confirmar_senha": "123456", "tipo": "aluno"
}, allow_redirects=False)
print(r.status_code, "redirect para /aluno/quiz" if r.status_code in (302, 303) and "/aluno/quiz" in str(r.headers.get("location", "")) else "FALHA: " + str(r.status_code))

print("\n=== GET /aluno/quiz ===")
r = client.get("/aluno/quiz")
print(r.status_code, "OK" if "Quiz de Carreira" in r.text else "FALHA")

print("\n=== POST /aluno/quiz (todas respostas desenvolvimento) ===")
dados = {"aluno_id": "1"}
for i in range(1, 26):
    dados[f"q{i}"] = "desenvolvimento"
r = client.post("/aluno/quiz", data=dados, allow_redirects=False)
print(r.status_code, "OK" if "Seu Resultado" in r.text else "FALHA: " + r.text[:200])

print("\n=== GET /login ===")
r = client.get("/login")
print(r.status_code, "OK" if "Entrar" in r.text else "FALHA")

print("\n=== POST /login (aluno ja fez quiz -> dashboard) ===")
r = client.post("/login", data={"username": usuario, "senha": "123456"}, allow_redirects=False)
print(r.status_code, "redirect para /dashboard" if r.status_code in (302, 303) and "/dashboard" in str(r.headers.get("location", "")) else "status: " + str(r.status_code), "cookies:", dict(r.cookies))

print("\n=== GET /dashboard ===")
r = client.get("/dashboard", allow_redirects=False)
print(r.status_code, "OK - dashboard com tipo Aluno" if r.status_code == 200 and "Aluno" in r.text else "FALHA: " + r.text[:200])

print("\n=== POST /logout ===")
r = client.post("/logout", allow_redirects=False)
print(r.status_code, "redirect" if r.status_code in (302, 303) else "FALHA")

print("\n=== Teste completo concluido ===")
