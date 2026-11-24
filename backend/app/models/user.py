from dataclasses import dataclass
from app.database import get_conn


@dataclass
class User:
    id: int
    username: str
    email: str
    password_hash: str
    created_at: str
    tipo: str = "aluno"
    quiz_feito: int = 0


class UserRepository:
    def create(self, username: str, email: str, password_hash: str, created_at: str, tipo: str = "aluno") -> User:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "INSERT INTO users (username, email, password_hash, created_at, tipo) VALUES (?, ?, ?, ?, ?)",
                (username, email, password_hash, created_at, tipo),
            )
            conn.commit()
            return self.get_by_username(username)
        finally:
            conn.close()

    def get_by_username(self, username: str) -> User | None:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT id, username, email, password_hash, created_at, tipo, quiz_feito FROM users WHERE username = ?",
                (username,),
            )
            row = c.fetchone()
            if not row:
                return None
            return User(**dict(row))
        finally:
            conn.close()

    def get_by_email(self, email: str) -> User | None:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT id, username, email, password_hash, created_at, tipo, quiz_feito FROM users WHERE email = ?",
                (email,),
            )
            row = c.fetchone()
            if not row:
                return None
            return User(**dict(row))
        finally:
            conn.close()

    def exists(self, username: str, email: str) -> bool:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "SELECT id FROM users WHERE username = ? OR email = ?",
                (username, email),
            )
            return c.fetchone() is not None
        finally:
            conn.close()

    # ✅ DEPOIS (em backend/app/models/user.py — responsabilidade no repositório certo)
    def registrar_quiz(self, user_id: int, carreira_recomendada: str) -> None:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "UPDATE users SET quiz_feito = 1, carreira_recomendada = ? WHERE id = ?",
                (carreira_recomendada, user_id),
            )
            conn.commit()
        finally:
            conn.close()
