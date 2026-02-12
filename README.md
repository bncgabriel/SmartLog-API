# SmartLog API

API REST para gestão logística com FastAPI, SQLAlchemy e PostgreSQL.

Domínios implementados:
- empresas
- permissões
- funcionários
- motoristas
- veículos
- operações
- cargas e descargas

## Tecnologias
- Python 3.10+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn
- Docker Compose

## Arquitetura atual

O projeto está organizado em camadas:
- `routes/`: camada HTTP (request/response)
- `services/`: regras de negócio e orquestração
- `repositories/`: acesso a dados (ORM)
- `models/`: modelos SQLAlchemy
- `schemas/`: contratos Pydantic
- `dependencies.py`: injeção de dependências
- `core/errors.py`: erros de domínio
- `main.py`: app, roteamento e handlers globais de erro

Fluxo de execução:
- Requisição HTTP -> `routes/*` -> `services/*` -> `repositories/*` -> banco

## Estrutura de pastas

```text
.
|-- core/
|-- repositories/
|-- services/
|-- routes/
|-- models/
|-- schemas/
|-- dependencies.py
|-- settings.py
|-- database.py
|-- main.py
|-- docker-compose.yml
`-- requirements.txt
```

## Configuração

Arquivos de ambiente:
- `.env.example` (versionado)
- `.env` (local, ignorado pelo Git)

Variáveis suportadas:
- `DB_HOST`
- `DB_PORT`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DATABASE_URL` (opcional, sobrescreve as anteriores)

Se `DATABASE_URL` não for definida, ela será montada automaticamente a partir de `DB_*`.

Crie seu arquivo local:

```bash
cp .env.example .env
```

## Banco de dados (PostgreSQL via Docker)

O `docker-compose.yml` usa as variáveis do `.env` para criar o banco e credenciais.

Subir:

```bash
docker compose up -d
```

Parar:

```bash
docker compose down
```

## Como iniciar localmente

1) Criar arquivo de ambiente:

```bash
cp .env.example .env
```

No Windows (PowerShell):

```powershell
Copy-Item .env.example .env
```

2) Seguir os passos do seu sistema operacional:

### Linux (bash/zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
docker compose up -d
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### macOS (bash/zsh)

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

## Endpoints (estado atual)

### Empresas (`/empresas`)
- `POST /` cria empresa
- `GET /` lista empresas
- `GET /{empresa_id}` busca empresa por ID
- `PUT /{empresa_id}` atualiza empresa
- `DELETE /{empresa_id}` remove empresa

### Permissões (`/permissoes`)
- `POST /` cria permissão (`201`)
- `GET /` lista permissões
- `GET /{permissao_id}` busca permissão por ID
- `PUT /{permissao_id}` atualiza permissão
- `DELETE /{permissao_id}` remove permissão (`204`)

### Funcionários (`/funcionarios`)
- `POST /` cria funcionário
- `GET /{funcionario_id}` busca funcionário por ID
- `GET /empresas/{id_empresa_vinculada}` lista funcionários por empresa
- `PUT /{funcionario_id}` atualiza funcionário
- `DELETE /{funcionario_id}` remove funcionário

### Motoristas (`/motoristas`)
- `POST /` cria motorista
- `GET /{motorista_id}` busca motorista por ID
- `PUT /{motorista_id}` atualiza motorista
- `DELETE /{motorista_id}` remove motorista

### Veículos (`/veiculos`)
- `POST /` cria veículo
- `GET /{placa_cavalo}` busca veículo por placa do cavalo
- `PUT /{placa_cavalo}` atualiza veículo por placa do cavalo
- `DELETE /{placa_cavalo}` remove veículo por placa do cavalo

### Operações (`/operacoes`)
- `POST /` cria operação
- `GET /` lista operações
- `GET /{operacao_id}` busca operação por ID
- `PUT /{operacao_id}` atualiza operação
- `DELETE /{operacao_id}` remove operação

### Cargas e Descargas (`/cargasdescargas`)
- `POST /` cria carga/descarga
- `GET /{carga_descarga_id}` busca carga/descarga por ID
- `PUT /{carga_descarga_id}` atualiza carga/descarga
- `DELETE /{carga_descarga_id}` remove carga/descarga

## Regras de negócio implementadas

`POST /cargasdescargas/`:
- valida se a operação informada existe
- valida se `pesagem` da carga não excede `pesagem_total` da operação
- decrementa `pesagem_total` da operação ao registrar a carga

## Tratamento de erros

Handlers globais em `main.py`:
- `NotFoundError` -> HTTP `404`
- `BusinessRuleError` -> HTTP `400`
- `DomainError` -> HTTP `400`

## Documentação interativa
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Observações importantes
- As tabelas são criadas automaticamente no startup via `Base.metadata.create_all(bind=engine)` em `main.py`.
- Este projeto não usa migrações (Alembic) atualmente.
