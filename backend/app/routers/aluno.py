from fastapi import APIRouter, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import random
import secrets
from datetime import datetime, timedelta, timezone

from app.controllers.dashboard import obter_usuario_logado
from app.controllers.aluno import cadastrar_aluno, calcular_resultado
from app.database import get_conn
from app.models.session import SessionRepository
from app.quiz_data import QUESTOES_TODAS, CAREERS
from app.config import SESSION_DURATION_DAYS

router = APIRouter()
templates = Jinja2Templates(directory="front/templates")
QUESTOES_POR_QUIZ = 25

session_repo = SessionRepository()


@router.get("/aluno/cadastro", response_class=HTMLResponse)
async def cadastro_aluno_page(request: Request):
    return RedirectResponse("/cadastro")


@router.post("/aluno/cadastro", response_class=HTMLResponse)
async def cadastro_aluno_post(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    confirmar_senha: str = Form(...),
):
    return RedirectResponse("/cadastro")


@router.get("/aluno/quiz", response_class=HTMLResponse)
async def quiz_page(request: Request):
    token = request.cookies.get("session_token")
    usuario = obter_usuario_logado(token)
    if not usuario:
        return RedirectResponse("/login")
    if usuario.get("quiz_feito"):
        return RedirectResponse("/dashboard")
    questoes_sorteadas = random.sample(QUESTOES_TODAS, QUESTOES_POR_QUIZ)
    questoes_ids = [str(q["id"]) for q in questoes_sorteadas]
    return templates.TemplateResponse(
        "aluno/quiz.html",
        {
            "request": request,
            "user": usuario,
            "questoes": questoes_sorteadas,
            "questoes_ids": questoes_ids,
            "total": len(questoes_sorteadas),
        },
    )


@router.post("/aluno/quiz", response_class=HTMLResponse)
async def quiz_resultado(request: Request):
    token = request.cookies.get("session_token")
    usuario = obter_usuario_logado(token)
    if not usuario:
        return RedirectResponse("/login")

    form = await request.form()
    questoes_ids = form.getlist("questoes_ids")
    respostas = {}
    for qid in questoes_ids:
        chave = f"q{qid}"
        valor = form.get(chave)
        if valor:
            respostas[int(qid)] = valor

    resultado = calcular_resultado(respostas)

    from app.models.quiz import ResultadoQuizRepository
    from datetime import datetime, timezone

    repo = ResultadoQuizRepository()
    aluno_id = usuario["id"]
    criado_em = datetime.now(timezone.utc).isoformat()
    repo.create(aluno_id, resultado["carreira"]["id"], resultado["pontos"], criado_em)

    # Marca o usuario como quiz feito e salva a carreira recomendada
    conn = get_conn()
    try:
        c = conn.cursor()
        c.execute(
            "UPDATE users SET quiz_feito = 1, carreira_recomendada = ? WHERE id = ?",
            (resultado["carreira"]["nome"], aluno_id),  # Salva o NOME, não o ID
        )
        conn.commit()
    finally:
        conn.close()

    # Atualiza a sessao com as informacoes atualizadas (quiz_feito e carreira_recomendada)
    expira = datetime.now(timezone.utc) + timedelta(days=SESSION_DURATION_DAYS)
    token_novo = secrets.token_urlsafe(32)
    session_repo.create(aluno_id, token_novo, expira)
    resp = templates.TemplateResponse(
        "aluno/resultado.html",
        {
            "request": request,
            "resultado": resultado,
        },
    )
    resp.set_cookie(
        "session_token",
        token_novo,
        httponly=True,
        secure=False,
        samesite="lax",
        expires=expira,
    )
    return resp


@router.get("/aluno/perfil/{aluno_id}", response_class=HTMLResponse)
async def perfil_aluno(request: Request, aluno_id: int):
    return templates.TemplateResponse(
        "aluno/perfil.html",
        {"request": request, "aluno_id": aluno_id},
    )
