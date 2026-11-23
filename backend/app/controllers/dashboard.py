from app.models.session import SessionRepository

session_repo = SessionRepository()


def obter_usuario_logado(token):
    return session_repo.get_by_token(token)
