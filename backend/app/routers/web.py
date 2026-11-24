from fastapi import APIRouter, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse

from app.controllers.web import (
    cadastro_page,
    cadastro_post,
    login_page,
    login_post,
    dashboard_get,
    logout,
)

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    token = request.cookies.get("session_token")
    from app.controllers.auth import obter_usuario_logado

    usuario = obter_usuario_logado(token)
    if usuario:
        return RedirectResponse("/dashboard")
    return RedirectResponse("/login")


@router.get("/login", response_class=HTMLResponse)
async def get_login(request: Request):
    return login_page(request)


@router.post("/login", response_class=HTMLResponse)
async def post_login(
    request: Request,
    username: str = Form(...),
    senha: str = Form(...),
):
    return login_post(request, username, senha)


@router.get("/cadastro", response_class=HTMLResponse)
async def get_cadastro(request: Request):
    return cadastro_page(request)


@router.post("/cadastro", response_class=HTMLResponse)
async def post_cadastro(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    confirmar_senha: str = Form(...),
    tipo: str = Form("aluno"),
):
    return cadastro_post(request, username, email, senha, confirmar_senha, tipo)


@router.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    return dashboard_get(request)


@router.post("/logout")
async def post_logout(request: Request):
    return logout(request)
