import os
import sys

_BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
_BACKEND_ROOT = os.path.dirname(_BACKEND_DIR)
_ROOT = os.path.dirname(_BACKEND_ROOT)
if _BACKEND_ROOT not in sys.path:
    sys.path.insert(0, _BACKEND_ROOT)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import init_db
from app.routers import web
from app.routers import aluno
from app.routers import trilha

app = FastAPI(title="Trilhar - MVP Login e Cadastro")

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(_ROOT, "front", "static")),
    name="static",
)

app.include_router(web.router)
app.include_router(aluno.router)
app.include_router(trilha.router)

init_db()
