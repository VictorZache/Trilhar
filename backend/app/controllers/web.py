from fastapi import Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime, timedelta, timezone
import secrets

from app.controllers.auth import cadastrar_usuario, autenticar_usuario
from app.controllers.auth import obter_usuario_logado
from app.config import SESSION_DURATION_DAYS
from app.models.session import SessionRepository

session_repo = SessionRepository()

templates = Jinja2Templates(directory="front/templates")

def landing_page(request: Request):
    token = request.cookies.get("session_token")
    usuario = obter_usuario_logado(token)
    return templates.TemplateResponse(
        "landing.html", {"request": request, "user": usuario}
    )


def cadastro_page(request: Request):
    return templates.TemplateResponse(
        "cadastro.html", {"request": request, "erro": None, "sucesso": None}
    )


def cadastro_post(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    confirmar_senha: str = Form(...),
    tipo: str = Form("aluno"),
):
    sucesso, mensagem, usuario = cadastrar_usuario(
        username, email, senha, confirmar_senha, tipo
    )
    if not sucesso:
        return templates.TemplateResponse(
            "cadastro.html",
            {"request": request, "erro": mensagem, "sucesso": None},
            status_code=400,
        )

    # Se cadastrou como aluno, fazer login automático e ir para o quiz
    if tipo == "aluno":
        expira = datetime.now(timezone.utc) + timedelta(days=SESSION_DURATION_DAYS)
        token = secrets.token_urlsafe(32)
        session_repo.create(usuario.id, token, expira)
        resp = RedirectResponse("/aluno/quiz", status_code=status.HTTP_302_FOUND)
        resp.set_cookie(
            "session_token",
            token,
            httponly=True,
            secure=False,
            samesite="lax",
            expires=expira,
        )
        return resp

    return templates.TemplateResponse(
        "cadastro.html",
        {"request": request, "erro": None, "sucesso": mensagem},
    )


def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "erro": None})


def login_post(
    request: Request,
    username: str = Form(...),
    senha: str = Form(...),
):
    sucesso, mensagem, usuario, token = autenticar_usuario(username, senha)
    if not sucesso:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "erro": mensagem},
            status_code=401,
        )

    expira = None
    from datetime import datetime, timedelta, timezone
    from app.config import SESSION_DURATION_DAYS

    expira = datetime.now(timezone.utc) + timedelta(days=SESSION_DURATION_DAYS)

    # Se for aluno e nao fez o quiz, redireciona para o quiz de carreira
    destino = "/aluno/quiz" if (
        usuario.get("tipo") == "aluno" and not usuario.get("quiz_feito")
    ) else "/dashboard"
    resp = RedirectResponse(destino, status_code=status.HTTP_302_FOUND)

    resp.set_cookie(
        "session_token",
        token,
        httponly=True,
        secure=False,
        samesite="lax",
        expires=expira,
    )
    return resp


def dashboard_get(request: Request):
    token = request.cookies.get("session_token")
    usuario = obter_usuario_logado(token)
    if not usuario:
        return RedirectResponse("/login")
    return templates.TemplateResponse(
        "dashboard.html", {"request": request, "user": usuario}
    )


# ✅ DEPOIS (apaga o cookie E remove a sessão do banco)
def logout(request: Request):
    token = request.cookies.get("session_token")
    if token:
        session_repo.delete(token)
    resp = RedirectResponse("/login", status_code=status.HTTP_302_FOUND)
    resp.delete_cookie("session_token")
    return resp
