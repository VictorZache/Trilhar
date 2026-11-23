from dataclasses import dataclass
from app.database import get_conn


@dataclass
class Aluno:
    id: int
    username: str
    email: str
    password_hash: str
    created_at: str
    quiz_feito: bool = False


class AlunoRepository:
    def create(self, username: str, email: str, password_hash: str, created_at: str) -> Aluno:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "INSERT INTO alunos (username, email, password_hash, created_at, quiz_feito) VALUES (?, ?, ?, ?, 0)",
                (username, email, password_hash, created_at),
            )
            conn.commit()
            return self.get_by_username(username)
        finally:
            conn.close()

    def get_by_username(self, username: str) -> Aluno | None:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT id, username, email, password_hash, created_at, quiz_feito FROM alunos WHERE username = ?",
                (username,),
            )
            row = c.fetchone()
            if not row:
                return None
            return Aluno(**dict(row))
        finally:
            conn.close()

    def get_by_email(self, email: str) -> Aluno | None:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT id, username, email, password_hash, created_at, quiz_feito FROM alunos WHERE email = ?",
                (email,),
            )
            row = c.fetchone()
            if not row:
                return None
            return Aluno(**dict(row))
        finally:
            conn.close()

    def exists(self, username: str, email: str) -> bool:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT id FROM alunos WHERE username = ? OR email = ?",
                (username, email),
            )
            return c.fetchone() is not None
        finally:
            conn.close()

    def marcar_quiz_feito(self, aluno_id: int) -> None:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute("UPDATE alunos SET quiz_feito = 1 WHERE id = ?", (aluno_id,))
            conn.commit()
        finally:
            conn.close()
