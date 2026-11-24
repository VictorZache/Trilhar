# ✅ DEPOIS (backend/tests/test_fluxo.py — seguro, com pytest e banco temporário)
import time
from fastapi.testclient import TestClient
from app import config, database
from app.main import app


def test_fluxo_completo_aluno(tmp_path, monkeypatch):
    # Isola o banco em uma pasta temporária que some após o teste
    db_temporario = tmp_path / "test.db"
    monkeypatch.setattr(config, "DB_PATH", str(db_temporario))
    monkeypatch.setattr(database, "DB_PATH", str(db_temporario))
    database.init_db()

    client = TestClient(app)
    usuario = f"estudante_{int(time.time())}"

    r = client.get("/cadastro")
    assert r.status_code == 200
    assert "Tipo de conta" in r.text

    r = client.post(
        "/cadastro",
        data={
            "username": usuario,
            "email": f"{usuario}@teste.com",
            "senha": "123456",
            "confirmar_senha": "123456",
            "tipo": "aluno",
        },
        follow_redirects=False,
    )
    assert r.status_code in (302, 303)
    assert "/aluno/quiz" in r.headers["location"]