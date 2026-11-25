import json
from fastapi import APIRouter, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.controllers.auth import obter_usuario_logado
from app.controllers.trilha import (
    listar_trilhas,
    obter_trilha,
    obter_missao,
    verificar_resposta,
)

router = APIRouter()
templates = Jinja2Templates(directory="front/templates")


def _usuario_logado(request: Request):
    token = request.cookies.get("session_token")
    return obter_usuario_logado(token)


@router.get("/estudante/trilhas", response_class=HTMLResponse)
async def trilhas_page(request: Request):
    usuario = _usuario_logado(request)
    if not usuario:
        return RedirectResponse("/login")
    trilhas = listar_trilhas(usuario["id"], usuario.get("carreira_recomendada"))
    return templates.TemplateResponse(
        "aluno/trilhas.html",
        {"request": request, "user": usuario, "trilhas": trilhas},
    )


@router.get("/estudante/trilha/{trilha_id}", response_class=HTMLResponse)
async def trilha_page(request: Request, trilha_id: int):
    usuario = _usuario_logado(request)
    if not usuario:
        return RedirectResponse("/login")
    dados = obter_trilha(trilha_id, usuario["id"])
    if not dados:
        return RedirectResponse("/estudante/trilhas")
    return templates.TemplateResponse(
        "aluno/trilha.html",
        {"request": request, "user": usuario, **dados},
    )


@router.get("/estudante/trilha/{trilha_id}/missao/{missao_id}", response_class=HTMLResponse)
async def missao_page(request: Request, trilha_id: int, missao_id: int):
    usuario = _usuario_logado(request)
    if not usuario:
        return RedirectResponse("/login")
    dados = obter_missao(missao_id, usuario["id"])
    if not dados:
        return RedirectResponse(f"/estudante/trilha/{trilha_id}")
    dados["trilha_id"] = trilha_id
    return templates.TemplateResponse(
        "aluno/trilha_missao.html",
        {"request": request, "user": usuario, **dados},
    )


@router.post("/estudante/trilha/{trilha_id}/missao/{missao_id}", response_class=HTMLResponse)
async def missao_responder(request: Request, trilha_id: int, missao_id: int):
    usuario = _usuario_logado(request)
    if not usuario:
        return RedirectResponse("/login")

    form = await request.form()
    tipo_jogo = form.get("tipo_jogo", "ordem")

    resposta_usuario = None
    if tipo_jogo == "ordem":
        ordem = form.getlist("ordem[]")
        resposta_usuario = ordem if ordem else None
    elif tipo_jogo == "categoria":
        # Vem como categoria_itemId
        respostas = {}
        for chave, valor in form.items():
            if chave.startswith("categoria_"):
                item_id = chave.replace("categoria_", "")
                respostas[item_id] = valor
        resposta_usuario = respostas if respostas else None
    elif tipo_jogo == "data":
        ordem = form.getlist("ordem[]")
        resposta_usuario = ordem if ordem else None
    elif tipo_jogo == "hq_investigacao":
        raw = form.get("resposta")
        if raw:
            try:
                resposta_usuario = json.loads(raw)
            except json.JSONDecodeError:
                resposta_usuario = None

    resultado = verificar_resposta(missao_id, usuario["id"], resposta_usuario)

    return templates.TemplateResponse(
        "aluno/trilha_resultado.html",
        {
            "request": request,
            "user": usuario,
            "trilha_id": trilha_id,
            "missao_id": missao_id,
            "correto": resultado["correto"],
            "mensagem": resultado["mensagem"],
        },
    )
