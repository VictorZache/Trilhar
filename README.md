# MVP Login e Cadastro

Projeto minimo com front + back em Python (FastAPI) contendo:
- Cadastro de usuario (username, email, senha com hash bcrypt)
- Login com sessão em cookie (httpOnly, expira em 7 dias)
- Dashboard protegido (redireciona para /login se nao autenticado)
- Logout
- Banco SQLite local (arquivo `data/app.db`)

## Como rodar

1. Crie o ambiente virtual e instale dependencias:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Inicie o servidor:

```powershell
.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8001
```

Ou, de dentro da pasta `backend`:

```powershell
cd backend
..\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

3. Acesse: http://127.0.0.1:8001

O banco `data/app.db` e criado automaticamente na primeira execucao.

Se o servidor nao iniciar, primeiro mate processos antigos:
```powershell
taskkill //F //IM python.exe
```
