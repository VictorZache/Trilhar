from fastapi import APIRouter, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import random
import secrets
from datetime import datetime, timedelta, timezone

from app.controllers.auth import obter_usuario_logado
from app.controllers.aluno import calcular_resultado
from app.database import get_conn
from app.models.session import SessionRepository
from app.models.user import UserRepository
from app.quiz_data import QUESTOES_TODAS, CAREERS
from app.config import SESSION_DURATION_DAYS

router = APIRouter()
templates = Jinja2Templates(directory="front/templates")
QUESTOES_POR_QUIZ = 25

session_repo = SessionRepository()




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


    ## ✅ DEPOIS (em backend/app/routers/aluno.py)
    # (lembre de importar UserRepository no topo: from app.models.user import UserRepository)
    UserRepository().registrar_quiz(aluno_id, resultado["carreira"]["nome"])

    return templates.TemplateResponse(
        "aluno/resultado.html",
        {"request": request, "user": usuario, "resultado": resultado},
    )

