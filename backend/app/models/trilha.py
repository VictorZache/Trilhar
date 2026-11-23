from dataclasses import dataclass
from app.database import get_conn


@dataclass
class Trilha:
    id: int
    nome: str
    descricao: str
    icone: str
    cor: str
    ordem: int


@dataclass
class Missao:
    id: int
    trilha_id: int
    titulo: str
    descricao: str
    tipo_jogo: str
    dados_jogo: str
    ordem: int


class TrilhaRepository:
    def listar_todas(self) -> list[Trilha]:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT id, nome, descricao, icone, cor, ordem FROM trilhas ORDER BY ordem"
            )
            return [Trilha(**dict(row)) for row in c.fetchall()]
        finally:
            conn.close()

    def get_por_id(self, trilha_id: int) -> Trilha | None:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT id, nome, descricao, icone, cor, ordem FROM trilhas WHERE id = ?",
                (trilha_id,),
            )
            row = c.fetchone()
            if not row:
                return None
            return Trilha(**dict(row))
        finally:
            conn.close()


class MissaoRepository:
    def listar_por_trilha(self, trilha_id: int) -> list[Missao]:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT id, trilha_id, titulo, descricao, tipo_jogo, dados_jogo, ordem FROM missoes WHERE trilha_id = ? ORDER BY ordem",
                (trilha_id,),
            )
            return [Missao(**dict(row)) for row in c.fetchall()]
        finally:
            conn.close()

    def get_por_id(self, missao_id: int) -> Missao | None:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT id, trilha_id, titulo, descricao, tipo_jogo, dados_jogo, ordem FROM missoes WHERE id = ?",
                (missao_id,),
            )
            row = c.fetchone()
            if not row:
                return None
            return Missao(**dict(row))
        finally:
            conn.close()


class ProgressoTrilhaRepository:
    def get_ou_criar(self, aluno_id: int, trilha_id: int):
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT id, aluno_id, trilha_id, missao_atual, concluida FROM progresso_trilha WHERE aluno_id = ? AND trilha_id = ?",
                (aluno_id, trilha_id),
            )
            row = c.fetchone()
            if row:
                return dict(row)
            c.execute(
                "INSERT INTO progresso_trilha (aluno_id, trilha_id, missao_atual, concluida) VALUES (?, ?, 1, 0)",
                (aluno_id, trilha_id),
            )
            conn.commit()
            return {"aluno_id": aluno_id, "trilha_id": trilha_id, "missao_atual": 1, "concluida": 0}
        finally:
            conn.close()

    def proxima_missao(self, aluno_id: int, trilha_id: int):
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "UPDATE progresso_trilha SET missao_atual = missao_atual + 1 WHERE aluno_id = ? AND trilha_id = ? AND concluida = 0",
                (aluno_id, trilha_id),
            )
            conn.commit()
        finally:
            conn.close()

    def concluir_trilha(self, aluno_id: int, trilha_id: int):
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "UPDATE progresso_trilha SET concluida = 1 WHERE aluno_id = ? AND trilha_id = ?",
                (aluno_id, trilha_id),
            )
            conn.commit()
        finally:
            conn.close()


class RespostaMissaoRepository:
    def salvar(self, aluno_id: int, missao_id: int, correto: bool):
        conn = get_conn()
        try:
            from datetime import datetime, timezone
            c = conn.cursor()
            c.execute(
                "INSERT INTO resposta_missao (aluno_id, missao_id, correto, criado_em) VALUES (?, ?, ?, ?)",
                (aluno_id, missao_id, 1 if correto else 0, datetime.now(timezone.utc).isoformat()),
            )
            conn.commit()
        finally:
            conn.close()

    def ultima_resposta(self, aluno_id: int, missao_id: int):
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT correto FROM resposta_missao WHERE aluno_id = ? AND missao_id = ? ORDER BY id DESC LIMIT 1",
                (aluno_id, missao_id),
            )
            row = c.fetchone()
            if not row:
                return None
            return dict(row)
        finally:
            conn.close()
