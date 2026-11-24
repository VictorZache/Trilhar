from datetime import datetime, timezone
from app.models.quiz import ResultadoQuizRepository
from app.quiz_data import CAREERS


resultado_repo = ResultadoQuizRepository()


def calcular_resultado(respostas: dict) -> dict:
    """
    respostas: dict {questao_id: carreira_id_escolhida}
    Retorna a carreira com mais pontos e o ranking completo.
    """
    pontos = {c["id"]: 0 for c in CAREERS}

    for qid, carreira_id in respostas.items():
        if carreira_id in pontos:
            pontos[carreira_id] += 1

    # Ranking ordenado
    ranking = sorted(pontos.items(), key=lambda x: x[1], reverse=True)
    carreira_vencedora_id = ranking[0][0]

    carreira_vencedora = next(c for c in CAREERS if c["id"] == carreira_vencedora_id)

    return {
        "carreira": carreira_vencedora,
        "pontos": pontos[carreira_vencedora_id],
        "total": max(len(respostas), 1),
        "ranking": ranking,
        "todas_carreiras": CAREERS,
    }



