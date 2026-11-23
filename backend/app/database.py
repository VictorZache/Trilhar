import os
import sqlite3
import json

from app.config import DB_PATH, DATA_DIR
from app.quiz_data import CAREERS

# Tipo de jogo para cada posicao de conhecimento (0-9)
TIPOS_JOGO = [
    "ordem",      # 0: arrastar e soltar em ordem
    "categoria",  # 1: arrastar para categoria
    "data",       # 2: ordenar por data
    "memoria",    # 3: jogo da memoria
    "quiz",       # 4: pergunta multipla escolha
    "arrastar",   # 5: arrastar item para destino correto
    "codigo",     # 6: arrastar blocos de codigo
    "quebra",     # 7: montar pecas do quebra-cabeca
    "labirinto",  # 8: caminho correto
    "simulador",  # 9: simular cenario
]


def get_conn():
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    try:
        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL,
                tipo TEXT DEFAULT 'aluno',
                quiz_feito INTEGER DEFAULT 0,
                carreira_recomendada TEXT
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
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL,
                quiz_feito INTEGER DEFAULT 0
            )
            """
        )
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS resultados_quiz (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id INTEGER NOT NULL,
                carreira TEXT NOT NULL,
                pontuacao INTEGER NOT NULL,
                criado_em TEXT NOT NULL,
                FOREIGN KEY (aluno_id) REFERENCES alunos(id)
            )
            """
        )
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS trilhas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                icone TEXT DEFAULT 'code',
                cor TEXT DEFAULT '#0052ff',
                ordem INTEGER DEFAULT 0
            )
            """
        )
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS missoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                trilha_id INTEGER NOT NULL,
                titulo TEXT NOT NULL,
                descricao TEXT,
                tipo_jogo TEXT DEFAULT 'ordem',
                dados_jogo TEXT,
                ordem INTEGER DEFAULT 0,
                FOREIGN KEY (trilha_id) REFERENCES trilhas(id)
            )
            """
        )
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS progresso_trilha (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id INTEGER NOT NULL,
                trilha_id INTEGER NOT NULL,
                missao_atual INTEGER DEFAULT 1,
                concluida INTEGER DEFAULT 0,
                FOREIGN KEY (aluno_id) REFERENCES users(id),
                FOREIGN KEY (trilha_id) REFERENCES trilhas(id),
                UNIQUE(aluno_id, trilha_id)
            )
            """
        )
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS resposta_missao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id INTEGER NOT NULL,
                missao_id INTEGER NOT NULL,
                correto INTEGER DEFAULT 0,
                criado_em TEXT NOT NULL,
                FOREIGN KEY (aluno_id) REFERENCES users(id),
                FOREIGN KEY (missao_id) REFERENCES missoes(id)
            )
            """
        )

        # Seed de dados iniciais (trilhas e missoes) a partir de quiz_data.py
        from app.quiz_data import CAREERS

        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM trilhas")
        if c.fetchone()[0] == 0:
            for carreira in CAREERS:
                c.execute(
                    "INSERT INTO trilhas (nome, descricao, icone, cor, ordem) VALUES (?, ?, ?, ?, ?)",
                    (
                        carreira["nome"],
                        carreira["descricao"],
                        carreira["icone"],
                        carreira["cor"],
                        1 if carreira["id"] == "desenvolvimento" else 99,
                    ),
                )
                trilha_id = c.lastrowid
                for i, conhecimento in enumerate(
                    carreira.get("conhecimento_necessario", []), 1
                ):
                    # conhecimento agora eh um dicionario com titulo, descricao, tipo_jogo, dados
                    tipo_jogo = conhecimento.get("tipo_jogo", TIPOS_JOGO[(i - 1) % len(TIPOS_JOGO)])
                    dados_jogo = json.dumps(
                        {"conhecimento": conhecimento, "tipo": tipo_jogo}
                    )
                    c.execute(
                        "INSERT INTO missoes (trilha_id, titulo, descricao, tipo_jogo, dados_jogo, ordem) VALUES (?, ?, ?, ?, ?, ?)",
                        (
                            trilha_id,
                            conhecimento.get("titulo", str(conhecimento)),
                            conhecimento.get("descricao", "Conteudo em breve."),
                            tipo_jogo,
                            dados_jogo,
                            i,
                        ),
                    )
        conn.commit()
    finally:
        conn.close()

    # Garante colunas tipo, quiz_feito e carreira_recomendada em bancos existentes
    conn = get_conn()
    try:
        c = conn.cursor()
        try:
            c.execute("ALTER TABLE users ADD COLUMN tipo TEXT DEFAULT 'aluno'")
        except sqlite3.OperationalError:
            pass
        try:
            c.execute("ALTER TABLE users ADD COLUMN quiz_feito INTEGER DEFAULT 0")
        except sqlite3.OperationalError:
            pass
        try:
            c.execute("ALTER TABLE users ADD COLUMN carreira_recomendada TEXT")
        except sqlite3.OperationalError:
            pass
        conn.commit()
    finally:
        conn.close()
