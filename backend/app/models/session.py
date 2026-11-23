from datetime import datetime, timedelta, timezone
from app.database import get_conn


class SessionRepository:
    def create(self, user_id: int, token: str, expires_at) -> None:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                "INSERT INTO sessions (user_id, token, expires_at) VALUES (?, ?, ?)",
                (user_id, token, expires_at.isoformat()),
            )
            conn.commit()
        finally:
            conn.close()

    def get_by_token(self, token: str):
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute(
                """
                SELECT u.id, u.username, u.email, u.tipo, u.quiz_feito, u.carreira_recomendada, s.expires_at
                FROM sessions s
                JOIN users u ON u.id = s.user_id
                WHERE s.token = ?
                """,
                (token,),
            )
            row = c.fetchone()
            if not row:
                return None
            expira = datetime.fromisoformat(row["expires_at"])
            if expira.tzinfo is None:
                expira = expira.replace(tzinfo=timezone.utc)
            if datetime.now(timezone.utc) > expira:
                return None
            return {
                "id": row["id"],
                "username": row["username"],
                "email": row["email"],
                "tipo": row["tipo"],
                "quiz_feito": row["quiz_feito"],
                "carreira_recomendada": row["carreira_recomendada"],
            }
        finally:
            conn.close()

    def delete(self, token: str) -> None:
        conn = get_conn()
        try:
            c = conn.cursor()
            c.execute("DELETE FROM sessions WHERE token = ?", (token,))
            conn.commit()
        finally:
            conn.close()
