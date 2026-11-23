from dataclasses import dataclass
from app.database import get_conn


@dataclass
class ResultadoQuiz:
    id: int
    aluno_id: int
    carreira: str
    pontuacao: int
    criado_em: str


class ResultadoQuizRepository:
    def create(self, aluno_id: int, carreira: str, pontuacao: int, criado_em: str) -> ResultadoQuiz:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "INSERT INTO resultados_quiz (aluno_id, carreira, pontuacao, criado_em) VALUES (?, ?, ?, ?)",
                (aluno_id, carreira, pontuacao, criado_em),
            )
            conn.commit()
            return self.get_by_aluno(aluno_id)
        finally:
            conn.close()

    def get_by_aluno(self, aluno_id: int) -> ResultadoQuiz | None:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT id, aluno_id, carreira, pontuacao, criado_em FROM resultados_quiz WHERE aluno_id = ? ORDER BY id DESC LIMIT 1",
                (aluno_id,),
            )
            row = c.fetchone()
            if not row:
                return None
            return ResultadoQuiz(**dict(row))
        finally:
            conn.close()

    def listar_todos(self) -> list[ResultadoQuiz]:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT id, aluno_id, carreira, pontuacao, criado_em FROM resultados_quiz ORDER BY id DESC"
            )
            return [ResultadoQuiz(**dict(row)) for row in c.fetchall()]
        finally:
            conn.close()
