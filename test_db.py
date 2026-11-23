import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend"))

print("CWD:", os.getcwd())
print("__file__:", __file__)

from app.config import DB_PATH, DATA_DIR
print("DB_PATH:", DB_PATH)
print("DATA_DIR:", DATA_DIR)

os.makedirs(DATA_DIR, exist_ok=True)

from app.database import get_conn, init_db
init_db()
print("init_db OK")

conn = get_conn()
c = conn.cursor()
c.execute("SELECT count(*) FROM users")
print("users count:", c.fetchone()[0])
conn.close()
