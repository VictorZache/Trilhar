# Trilhar - MVP

Plataforma educacional gamificada para orientacao vocacional na area de TI. Sistema completo com front-end e back-end em Python (FastAPI), banco SQLite local, autenticacao com sessao em cookie, quiz de carreira, trilhas de aprendizagem e missoes com minigames interativos.

---

## Funcionalidades

- **Cadastro e login**: usuario, email, senha com hash bcrypt, sessao em cookie httpOnly (expira em 7 dias), tipos de conta (aluno / professor)
- **Dashboard protegido**: redireciona para login se nao autenticado, exibe informacoes do usuario e acoes disponiveis
- **Quiz de carreira**: 25 perguntas sorteadas de um banco de 75 questoes, define a carreira recomendada entre 10 areas de TI
- **Trilhas de aprendizagem**: cada carreira tem uma trilha com 10 missoes (uma por conhecimento necessario), totalizando 100 missoes
- **Missoes com minigames**: cada missão tem conteudo teorico e um tipo de jogo específico (sequencia, sql, estatistica, wireframe, etc.)
- **Progresso**: controle de missao atual e trilha concluida por aluno
- **Banco de dados**: SQLite local em `data/app.db`, criado automaticamente na primeira execucao

---

## Stack tecnologica

| Camada | Tecnologia |
|--------|------------|
| Backend | Python 3.14 + FastAPI |
| Banco de dados | SQLite |
| Autenticacao | bcrypt + cookie httpOnly |
| Templates | Jinja2 |
| Front-end | HTML5 + CSS3 (Inter font, design responsivo) |
| Servidor | Uvicorn |

---

## Arquitetura (MVC)

O projeto segue padrao Model-View-Controller separado por responsabilidade:

```
trilhar/
├── backend/
│   ├── app/
│   │   ├── main.py              # Entrada FastAPI, monta static e rotas
│   │   ├── config.py            # Configuracoes (DB_PATH, DATA_DIR, SESSION_DURATION_DAYS)
│   │   ├── database.py          # init_db, tabelas, seed de trilhas e missoes
│   │   ├── quiz_data.py         # 10 carreiras, 100 missoes, 75 questoes do quiz
│   │   ├── models/
│   │   │   ├── trilha.py        # Repositorios de trilha, missoes, progresso, resposta
│   │   │   ├── user.py          # User dataclass
│   │   │   ├── aluno.py         # AlunoRepository
│   │   │   ├── quiz.py          # ResultadoQuizRepository
│   │   │   └── session.py       # SessionRepository
│   │   ├── controllers/
│   │   │   ├── web.py           # Logica de cadastro, login, dashboard, logout
│   │   │   ├── auth.py          # cadastrar_usuario, autenticar_usuario
│   │   │   ├── aluno.py         # cadastrar_aluno, calcular_resultado
│   │   │   └── trilha.py        # listar_trilhas, obter_trilha, obter_missao, verificar_resposta
│   │   └── routers/
│   │       ├── web.py           # Rotas web (/, /login, /cadastro, /dashboard, /logout)
│   │       ├── aluno.py         # Rotas de aluno (/aluno/cadastro, /aluno/quiz)
│   │       └── trilha.py        # Rotas de trilha (/estudante/trilhas, /estudante/trilha/{id}, /estudante/trilha/{id}/missao/{id})
│   └── ...
├── front/
│   ├── static/
│   │   ├── style.css            # Sistema de design completo (variaveis CSS, componentes)
│   │   └── toast.js             # Notificacoes toast
│   └── templates/
│       ├── base.html            # Layout base com navbar fixa
│       ├── login.html
│       ├── cadastro.html
│       ├── dashboard.html
│       └── aluno/
│           ├── quiz.html
│           ├── resultado.html
│           ├── trilhas.html
│           ├── trilha.html
│           ├── trilha_missao.html
│           └── trilha_resultado.html
├── data/
│   └── app.db                   # Banco SQLite (criado automaticamente)
├── requirements.txt
└── README.md
```

---

## Banco de dados

O banco `data/app.db` e criado automaticamente na primeira execucao via `init_db()`. Tabelas:

- **users**: id, username, email, password_hash, created_at, tipo, quiz_feito, carreira_recomendada
- **sessions**: id, user_id, token, expires_at
- **alunos**: id, username, email, password_hash, created_at, quiz_feito
- **resultados_quiz**: id, aluno_id, carreira, pontuacao, criado_em
- **trilhas**: id, nome, descricao, icone, cor, ordem
- **missoes**: id, trilha_id, titulo, descricao, tipo_jogo, dados_jogo, ordem
- **progresso_trilha**: id, aluno_id, trilha_id, missao_atual, concluida
- **resposta_missao**: id, aluno_id, missao_id, correto, criado_em

---

## Como rodar

### 1. Crie o ambiente virtual e instale dependencias

**PowerShell:**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**CMD:**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

### 2. Inicie o servidor

Na raiz do projeto (`C:\Users\ZachW\Downloads\trilhar`):

```bash
export PYTHONPATH=backend
.venv/Scripts/python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001
```

Ou, de dentro da pasta `backend`:

```bash
cd backend
export PYTHONPATH=..
.venv/Scripts/python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001
```

### 3. Acesse

- http://127.0.0.1:8001 — redireciona para login ou dashboard
- http://127.0.0.1:8001/login — pagina de login
- http://127.0.0.1:8001/cadastro — pagina de cadastro
- http://127.0.0.1:8001/dashboard — painel protegido
- http://127.0.0.1:8001/aluno/quiz — quiz de carreira
- http://127.0.0.1:8001/estudante/trilhas — lista de trilhas

---

## Rotas da aplicacao

| Metodo | Rota | Descricao |
|--------|------|-----------|
| GET | / | Redirect para /login ou /dashboard |
| GET | /login | Pagina de login |
| POST | /login | Autenticacao |
| GET | /cadastro | Pagina de cadastro |
| POST | /cadastro | Criar usuario |
| GET | /dashboard | Painel protegido |
| POST | /logout | Encerrar sessao |
| GET | /aluno/quiz | Pagina do quiz |
| POST | /aluno/quiz | Enviar respostas e calcular resultado |
| GET | /estudante/trilhas | Listar trilhas recomendadas |
| GET | /estudante/trilha/{id} | Detalhe da trilha com missoes |
| GET | /estudante/trilha/{id}/missao/{id} | Pagina de uma missao |
| POST | /estudante/trilha/{id}/missao/{id} | Responder missao |

---

## Quiz de carreira

O quiz contem 75 questoes no total. A cada execucao, 25 questoes sao sorteadas aleatoriamente. Cada resposta adiciona pontos a uma ou mais carreiras. Ao final, a carreira com maior pontuacao e recomendada e salva no banco (`carreira_recomendada` na tabela `users`). O quiz aparece apenas na primeira vez que o aluno acessa; apos concluido, nao e exibido novamente.

As 10 carreiras disponiveis:

1. Desenvolvimento de Software
2. Analise de Dados
3. Seguranca da Informacao
4. Computacao em Nuvem
5. Redes e Infraestrutura
6. Banco de Dados
7. DevOps
8. Product Owner / Scrum Master
9. QA / Testes de Software
10. Design UX/UI

---

## Trilhas e missoes

Cada carreira possui uma trilha com 10 missoes, uma por conhecimento necessario. Total: 100 missoes no banco.

Cada missao tem:
- **Titulo**: nome do conhecimento (ex: Logica de Programacao)
- **Descricao teorica**: explicacao do conteudo
- **Tipo de jogo**: identificador do minigame (ex: sequencia, sql, estatistica, wireframe, etc.)
- **Dados do jogo**: JSON com informacoes para renderizar o jogo no front-end

Tipos de jogo implementados: ordem, categoria, data, conceito, senha, phishing, criptografia, firewall, estatistica, grafico, planilha, limpeza, probabilidade, pandas, storytelling, etica, caixa_memoria, repeticao, decisao, funcao, lista, classe_objeto, commit, html_css_js, armazenamento, maquina_virtual, banco_nuvem, seguranca_nuvem, migracao, custo, provedor, servidor_cliente, ip, dispositivo, protocolo, cabo_wifi, servidor_estacao, topologia, seguranca_rede, so_servidor, monitoramento, tabela, chave, relacionamento, normalizacao, backup, seguranca_dados, modelagem, tipo_banco, ci, cd, docker, kubernetes, git, teste_automatizado, monitoramento_app, iac, colaboracao, agile, historia, backlog, sprint, requisitos, comunicacao, priorizacao, metricas, reuniao, caso_teste, bug, usabilidade, regressao, ferramenta, qc, ciclo_vida, documentacao, ui, cores, tipografia, wireframe, responsivo, acessibilidade, ferramenta_design, pesquisa, teste_usabilidade.

---

## Variaveis de configuracao (`backend/app/config.py`)

- `DB_PATH`: caminho do banco SQLite
- `DATA_DIR`: pasta de dados
- `SESSION_DURATION_DAYS`: duracao da sessao em dias (padrao 7)

---

## Git e GitHub

```bash
cd "C:/Users/ZachW/Downloads/trilhar"
git init
git add .
git commit -m "feat: versao inicial do projeto Trilhar"
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
git branch -M main
git push -u origin main
```

Arquivos ignorados (`.gitignore`):

```
.venv/
__pycache__/
*.pyc
*.db
*.sqlite
.env
data/
```

---

## Proximos passos

- Implementar visual interativo para os demais tipos de jogo (atualmente so ordem, categoria e data tem visual customizado; os demais usam fallback generico com conteudo teorico)
- Area do professor (atualmente placeholder)
- Sistema de pontuacao e badge por missao concluida
- Exportacao de relatorios de progresso

---

## Observacoes

- O banco `data/app.db` e recriado automaticamente se nao existir
- Se a porta 8001 estiver ocupada, mate processos antigos: `taskkill //F //IM python.exe`
- O servidor deve ser executado da raiz do projeto com `PYTHONPATH=backend` definido
- Nao commite o arquivo `data/app.db` nem a pasta `.venv/`
