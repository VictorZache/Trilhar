import bcrypt
from datetime import datetime, timedelta, timezone
import secrets

from app.config import SESSION_DURATION_DAYS
from app.models.user import UserRepository
from app.models.session import SessionRepository


user_repo = UserRepository()
session_repo = SessionRepository()


def hash_senha(senha: str) -> str:
    return bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verificar_senha(senha_plana: str, hash_armazenado: str) -> bool:
    return bcrypt.checkpw(senha_plana.encode("utf-8"), hash_armazenado.encode("utf-8"))


def cadastrar_usuario(username: str, email: str, senha: str, confirmar_senha: str, tipo: str = "aluno"):
    """Retorna (sucesso: bool, mensagem: str, usuario: User|None)"""
    if senha != confirmar_senha:
        return False, "As senhas nao coincidem", None

    if user_repo.exists(username, email):
        return False, "Usuario ou email ja cadastrado", None

    criado_em = datetime.now(timezone.utc).isoformat()
    user_repo.create(username, email, hash_senha(senha), criado_em, tipo)
    usuario = user_repo.get_by_username(username)
    return True, "Conta criada com sucesso. Faca login.", usuario


def autenticar_usuario(username: str, senha: str):
    """Retorna (sucesso: bool, mensagem: str, usuario: dict|None, token: str|None)"""
    usuario = user_repo.get_by_username(username)
    if not usuario or not verificar_senha(senha, usuario.password_hash):
        return False, "Usuario ou senha invalidos", None, None

    token = secrets.token_urlsafe(32)
    expira = datetime.now(timezone.utc) + timedelta(days=SESSION_DURATION_DAYS)
    session_repo.create(usuario.id, token, expira)
    return True, None, {
        "id": usuario.id,
        "username": usuario.username,
        "email": usuario.email,
        "tipo": getattr(usuario, "tipo", "aluno"),
        "quiz_feito": getattr(usuario, "quiz_feito", 0),
    }, token

def obter_usuario_logado(token: str | None):
    return session_repo.get_by_token(token)
