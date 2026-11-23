import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend"))

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "app.db")
if os.path.exists(db_path):
    os.remove(db_path)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

import time
timestamp = str(int(time.time()))
usuario = f"estudante_{timestamp}"
email = f"{usuario}@teste.com"

# Teste 1: página de cadastro de aluno
r = client.get("/aluno/cadastro")
print("GET /aluno/cadastro:", r.status_code, "OK" if "Cadastro de Aluno" in r.text else "FALHA")

# Teste 2: cadastrar aluno
r = client.post("/aluno/cadastro", data={"username": usuario, "email": email, "senha": "123456", "confirmar_senha": "123456"})
print("POST /aluno/cadastro:", r.status_code, "OK" if "sucesso" in r.text.lower() else "FALHA: " + r.text[:200])

# Teste 3: página do quiz
r = client.get("/aluno/quiz")
print("GET /aluno/quiz:", r.status_code, "OK" if "Quiz de Carreira" in r.text else "FALHA")

# Teste 4: responder quiz (todas as respostas para "desenvolvimento")
dados = {"aluno_id": "1"}
for i in range(1, 26):
    dados[f"q{i}"] = "desenvolvimento"
r = client.post("/aluno/quiz", data=dados)
print("POST /aluno/quiz:", r.status_code, "OK" if "Seu Resultado" in r.text else "FALHA: " + r.text[:200])

print("\nTestes do modulo de estudante concluidos.")
