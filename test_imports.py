import os, sys
sys.path.insert(0, os.path.join(os.getcwd(), "backend"))

# Tentar importar tudo
print("Importando config...")
from app.config import DB_PATH, DATA_DIR, SESSION_DURATION_DAYS
print("  OK")

print("Importando database...")
from app.database import get_conn, init_db
print("  OK")

print("Importando models.user...")
from app.models.user import User, UserRepository
print("  OK")

print("Importando models.session...")
from app.models.session import SessionRepository
print("  OK")

print("Importando controllers.auth...")
from app.controllers.auth import hash_senha, verificar_senha, cadastrar_usuario, autenticar_usuario
print("  OK")

print("Importando controllers.dashboard...")
from app.controllers.dashboard import obter_usuario_logado
print("  OK")

print("Importando controllers.web...")
from app.controllers.web import cadastro_page, cadastro_post, login_page, login_post, dashboard_get, logout
print("  OK")

print("Importando routers.web...")
from app.routers import web
print("  OK")

print("Importando app.main...")
from app.main import app
print("  OK")

print("\nTodas as importacoes funcionaram!")

# Testar bcrypt diretamente
import bcrypt
h = bcrypt.hashpw(b"senha123", bcrypt.gensalt())
ok = bcrypt.checkpw(b"senha123", h)
print(f"bcrypt funciona: hash={h[:20]}..., check={ok}")
