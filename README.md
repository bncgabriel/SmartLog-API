# SmartLog API

API REST em FastAPI para gerenciamento de:
- empresas
- permissões
- funcionários
- motoristas
- veículos
- operações
- cargas e descargas

## Stack
- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker Compose (para subir o banco)

## Estrutura do projeto

```text
.
|-- main.py
|-- database.py
|-- docker-compose.yml
|-- models/
|-- schemas/
`-- routes/
```

## Pré-requisitos
- Python 3.12+
- Docker e Docker Compose

## Banco de dados (PostgreSQL)

Este projeto já possui `docker-compose.yml` para o banco:
- host: `localhost`
- porta: `1001`
- database: `smartlog`
- user: `bncgabriel`
- password: `postgres`

Subir banco:

```bash
docker compose up -d
```

Parar banco:

```bash
docker compose down
```

## Instalação de dependências

```bash
pip install -r requirements.txt
```

## Como iniciar a aplicação por sistema operacional

### Linux (bash/zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
docker compose up -d
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### macOS (zsh/bash)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
docker compose up -d
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Windows (PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
docker compose up -d
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Windows (CMD)

```bat
py -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
docker compose up -d
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Acesso local
- API: `http://localhost:8000`
- Swagger: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Observações importantes
- A conexão do banco está definida diretamente em `database.py` (variável `SQLALCHEMY_DATABASE_URL`).
- Se precisar usar outro usuário/senha/porta, ajuste essa string em `database.py`.
- Evite usar os diretórios `linux-venv` e `smartlog-venv` versionados no repositório; prefira criar um ambiente novo com os comandos acima.
