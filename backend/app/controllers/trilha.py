import json
from app.models.trilha import TrilhaRepository, MissaoRepository, ProgressoTrilhaRepository, RespostaMissaoRepository
from app.quiz_data import CAREERS

trilha_repo = TrilhaRepository()
missao_repo = MissaoRepository()
progresso_repo = ProgressoTrilhaRepository()
resposta_repo = RespostaMissaoRepository()


def listar_trilhas(aluno_id: int, carreira_recomendada: str | None = None) -> list[dict]:
    trilhas = trilha_repo.listar_todas()
    resultado = []
    for t in trilhas:
        # Mostrar apenas a trilha recomendada pelo quiz
        eh_introdutoria = t.ordem == 0
        if carreira_recomendada and not eh_introdutoria and t.nome != carreira_recomendada:
            continue
        progresso = progresso_repo.get_ou_criar(aluno_id, t.id)
        resultado.append({
            "id": t.id,
            "nome": t.nome,
            "descricao": t.descricao,
            "icone": t.icone,
            "cor": t.cor,
            "missao_atual": progresso["missao_atual"],
            "concluida": progresso["concluida"],
            "recomendada": t.nome == carreira_recomendada,
            "introdutoria": eh_introdutoria,
        })
    return resultado


def obter_trilha(trilha_id: int, aluno_id: int):
    trilha = trilha_repo.get_por_id(trilha_id)
    if not trilha:
        return None
    missoes = missao_repo.listar_por_trilha(trilha_id)
    progresso = progresso_repo.get_ou_criar(aluno_id, trilha_id)
    return {
        "trilha": trilha,
        "missoes": missoes,
        "progresso": progresso,
    }


def obter_missao(missao_id: int, aluno_id: int):
    missao = missao_repo.get_por_id(missao_id)
    if not missao:
        return None
    import json
    dados = json.loads(missao.dados_jogo) if missao.dados_jogo else {}
    ultima = resposta_repo.ultima_resposta(aluno_id, missao_id)
    return {
        "missao": missao,
        "missao_id": missao_id,
        "dados": dados,
        "ultima_correta": ultima["correto"] if ultima else None,
    }


def _validar_hq_investigacao(dados: dict, resposta_usuario) -> tuple[bool, str]:
    if not isinstance(resposta_usuario, dict):
        return False, "Formato de resposta inválido para a investigação em HQ."

    cenas_esperadas = [c["id"] for c in dados.get("cenas", [])]
    cenas_feitas = set(resposta_usuario.get("cenas_concluidas", []))
    if not all(cid in cenas_feitas for cid in cenas_esperadas):
        return False, "Conclua todas as cenas da investigação antes de finalizar a missão."

    quiz_cfg = dados.get("fechamento", {}).get("quiz", {})
    questoes = quiz_cfg.get("questoes", [])
    nota_minima = quiz_cfg.get("nota_minima", len(questoes))
    respostas_quiz = resposta_usuario.get("respostas_quiz", {})

    acertos = sum(1 for q in questoes if respostas_quiz.get(q["id"]) == q["correta_idx"])
    if acertos >= nota_minima:
        return True, f"Missão concluída! Você completou a investigação e acertou {acertos} de {len(questoes)} no quiz."
    return False, f"Você acertou {acertos} de {len(questoes)} no quiz complementar (mínimo {nota_minima}). Revise a leitura e tente novamente!"


def verificar_resposta(missao_id: int, aluno_id: int, resposta_usuario):
    missao = missao_repo.get_por_id(missao_id)
    if not missao:
        return {"correto": False, "mensagem": "Missão não encontrada."}

    if not resposta_usuario:
        return {"correto": False, "mensagem": "Envie uma resposta antes de continuar."}

    import json
    dados = json.loads(missao.dados_jogo) if missao.dados_jogo else {}
    correto = False
    mensagem = ""

    if missao.tipo_jogo == "ordem":
        ordem_correta = dados.get("ordem_correta", [])
        correto = resposta_usuario == ordem_correta
        mensagem = "Parabéns! Você organizou corretamente." if correto else "Não quite, tente novamente."
    elif missao.tipo_jogo == "categoria":
        # resposta_usuario vem como dicionário {item_id: categoria_id}
        corretas = dados.get("corretas", {})
        acertos = sum(1 for k, v in resposta_usuario.items() if corretas.get(k) == v)
        total = len(corretas)
        correto = acertos == total
        mensagem = f"Você acertou {acertos} de {total}." if not correto else "Parabém! Você classificou tudo corretamente."
    elif missao.tipo_jogo == "data":
        ordem_correta = dados.get("ordem_correta", [])
        correto = resposta_usuario == ordem_correta
        mensagem = "Parabéns! Você ordenou corretamente por data." if correto else "Não quite, verifique as datas."
    elif missao.tipo_jogo == "hq_investigacao":
        correto, mensagem = _validar_hq_investigacao(dados, resposta_usuario)

    resposta_repo.salvar(aluno_id, missao_id, correto)

    # Se correto, avança a missão
    if correto:
        progresso_repo.proxima_missao(aluno_id, missao.trilha_id)
        # Verifica se concluiu todas
        progresso = progresso_repo.get_ou_criar(aluno_id, missao.trilha_id)
        missoes = missao_repo.listar_por_trilha(missao.trilha_id)
        if progresso["missao_atual"] > len(missoes):
            progresso_repo.concluir_trilha(aluno_id, missao.trilha_id)

    return {"correto": correto, "mensagem": mensagem}
