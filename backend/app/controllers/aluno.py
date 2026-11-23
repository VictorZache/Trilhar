from datetime import datetime, timezone
from app.models.aluno import AlunoRepository
from app.models.quiz import ResultadoQuizRepository
from app.quiz_data import CAREERS, QUESTOES_TODAS


aluno_repo = AlunoRepository()
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


def cadastrar_aluno(username: str, email: str, senha: str, confirmar_senha: str):
    if senha != confirmar_senha:
        return False, "As senhas nao coincidem", None

    if aluno_repo.exists(username, email):
        return False, "Usuario ou email ja cadastrado", None

    import bcrypt

    criado_em = datetime.now(timezone.utc).isoformat()
    hash_senha = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    aluno_repo.create(username, email, hash_senha, criado_em)
    aluno = aluno_repo.get_by_username(username)
    return True, "Conta de aluno criada com sucesso.", aluno
