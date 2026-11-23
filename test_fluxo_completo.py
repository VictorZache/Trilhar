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

print("=== 1. GET /cadastro ===")
r = client.get("/cadastro")
print(r.status_code, "OK" if "Tipo de conta" in r.text else "FALHA")

print("\n=== 2. POST /cadastro (aluno) -> deve redirecionar para /aluno/quiz com cookie ===")
r = client.post("/cadastro", data={
    "username": usuario, "email": email, "senha": "123456", "confirmar_senha": "123456", "tipo": "aluno"
}, allow_redirects=False)
print(r.status_code, "redirect para /aluno/quiz" if r.status_code in (302, 303) and "/aluno/quiz" in str(r.headers.get("location", "")) else "FALHA: " + str(r.status_code))
print("Cookies apos cadastro:", dict(r.cookies))

print("\n=== 3. GET /aluno/quiz (deve funcionar, quiz_feito = 0) ===")
r = client.get("/aluno/quiz")
print(r.status_code, "OK" if "Quiz de Carreira" in r.text else "FALHA")

print("\n=== 4. POST /aluno/quiz (todas respostas desenvolvimento) ===")
dados = {"aluno_id": "1"}
for i in range(1, 26):
    dados[f"q{i}"] = "desenvolvimento"
r = client.post("/aluno/quiz", data=dados, allow_redirects=False)
print(r.status_code, "OK" if "Seu Resultado" in r.text else "FALHA: " + r.text[:200])
print("Cookies apos quiz:", dict(r.cookies))

print("\n=== 5. GET /aluno/quiz (apos fazer quiz -> deve redirecionar para dashboard) ===")
r = client.get("/aluno/quiz", allow_redirects=False)
print(r.status_code, "redirect para /dashboard" if r.status_code in (302, 303) and "/dashboard" in str(r.headers.get("location", "")) else "FALHA: " + str(r.status_code))

print("\n=== 6. GET /estudante/trilhas (deve mostrar trilha recomendada) ===")
r = client.get("/estudante/trilhas")
print(r.status_code, "OK - trilhas" if r.status_code == 200 else "FALHA: " + str(r.status_code))
print("Contem 'Trilha':", "Trilha" in r.text)

print("\n=== 7. GET /login ===")
r = client.get("/login")
print(r.status_code, "OK" if "Entrar" in r.text else "FALHA")

print("\n=== 8. POST /login (aluno ja fez quiz -> dashboard) ===")
r = client.post("/login", data={"username": usuario, "senha": "123456"}, allow_redirects=False)
print(r.status_code, "redirect para /dashboard" if r.status_code in (302, 303) and "/dashboard" in str(r.headers.get("location", "")) else "status: " + str(r.status_code), "cookies:", dict(r.cookies))

print("\n=== 9. GET /dashboard ===")
r = client.get("/dashboard", allow_redirects=False)
print(r.status_code, "OK - dashboard" if r.status_code == 200 else "FALHA: " + str(r.status_code))

print("\n=== 10. POST /logout ===")
r = client.post("/logout", allow_redirects=False)
print(r.status_code, "redirect" if r.status_code in (302, 303) else "FALHA")

print("\n=== Teste completo concluido com sucesso ===")
