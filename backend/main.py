import os
import secrets
import sqlite3
from datetime import datetime, timedelta, timezone

from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import bcrypt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "app.db")
SESSION_DURATION_DAYS = 7

app = FastAPI(title="MVP Login e Cadastro")

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(PROJECT_DIR, "front", "static")),
    name="static",
)
templates = Jinja2Templates(directory=os.path.join(PROJECT_DIR, "front", "templates"))

def hash_senha(senha: str) -> str:
    return bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verificar_senha(senha_plana: str, hash_armazenado: str) -> bool:
    return bcrypt.checkpw(senha_plana.encode("utf-8"), hash_armazenado.encode("utf-8"))


def get_conn():
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            token TEXT UNIQUE NOT NULL,
            expires_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
    )
    conn.commit()
    conn.close()


init_db()


def obter_usuario_por_token(token: str | None, conn: sqlite3.Connection):
    if not token:
        return None
    c = conn.cursor()
    c.execute(
        """
        SELECT u.id, u.username, u.email, s.expires_at
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
    return {"id": row["id"], "username": row["username"], "email": row["email"]}


def usuario_autenticado(request: Request, conn: sqlite3.Connection):
    token = request.cookies.get("session_token")
    return obter_usuario_por_token(token, conn)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    conn = get_conn()
    try:
        user = usuario_autenticado(request, conn)
    finally:
        conn.close()
    if user:
        return RedirectResponse("/dashboard")
    return RedirectResponse("/login")


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "erro": None})


@app.post("/login", response_class=HTMLResponse)
async def login(
    request: Request, username: str = Form(...), senha: str = Form(...)
):
    conn = get_conn()
    try:
        c = conn.cursor()
        c.execute(
            "SELECT id, username, password_hash FROM users WHERE username = ?",
            (username,),
        )
        row = c.fetchone()
        if not row or not verificar_senha(senha, row["password_hash"]):
            return templates.TemplateResponse(
                "login.html",
                {"request": request, "erro": "Usuario ou senha invalidos"},
                status_code=401,
            )
        token = secrets.token_urlsafe(32)
        expira = datetime.now(timezone.utc) + timedelta(days=SESSION_DURATION_DAYS)
        c.execute(
            "INSERT INTO sessions (user_id, token, expires_at) VALUES (?, ?, ?)",
            (row["id"], token, expira.isoformat()),
        )
        conn.commit()
        resp = RedirectResponse("/dashboard", status_code=status.HTTP_302_FOUND)
        resp.set_cookie(
            "session_token",
            token,
            httponly=True,
            secure=False,
            samesite="lax",
            expires=expira,
        )
        return resp
    finally:
        conn.close()


@app.get("/cadastro", response_class=HTMLResponse)
async def cadastro_page(request: Request):
    return templates.TemplateResponse(
        "cadastro.html", {"request": request, "erro": None, "sucesso": None}
    )


@app.post("/cadastro", response_class=HTMLResponse)
async def cadastro(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    confirmar_senha: str = Form(...),
):
    conn = get_conn()
    try:
        if senha != confirmar_senha:
            return templates.TemplateResponse(
                "cadastro.html",
                {
                    "request": request,
                    "erro": "As senhas nao coincidem",
                    "sucesso": None,
                },
                status_code=400,
            )
        c = conn.cursor()
        c.execute(
            "SELECT id FROM users WHERE username = ? OR email = ?",
            (username, email),
        )
        if c.fetchone():
            return templates.TemplateResponse(
                "cadastro.html",
                {
                    "request": request,
                    "erro": "Usuario ou email ja cadastrado",
                    "sucesso": None,
                },
                status_code=400,
            )
        criado_em = datetime.now(timezone.utc).isoformat()
        c.execute(
            "INSERT INTO users (username, email, password_hash, created_at) VALUES (?, ?, ?, ?)",
            (username, email, hash_senha(senha), criado_em),
        )
        conn.commit()
        return templates.TemplateResponse(
            "cadastro.html",
            {
                "request": request,
                "erro": None,
                "sucesso": "Conta criada com sucesso. Faca login.",
            },
        )
    finally:
        conn.close()


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    conn = get_conn()
    try:
        user = usuario_autenticado(request, conn)
    finally:
        conn.close()
    if not user:
        return RedirectResponse("/login")
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})


@app.post("/logout")
async def logout():
    resp = RedirectResponse("/login", status_code=status.HTTP_302_FOUND)
    resp.delete_cookie("session_token")
    return resp
