from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from routes import permissao

smartlog = FastAPI()

class Operacao(BaseModel):
    navio_operacao: str
    pais_orig: str
    tipo_carga: str
    pesagem_total: float
    periodo: str

operacao_db = []

@smartlog.post("/operacoes", response_model= Operacao)
async def cadastrar_operacao(operacao: Operacao):
    permissoes_db.append(operacao)
    return operacao

@smartlog.get("/operacoes/", response_model=List[Operacao])
async def read_empresas():
    return operacao_db

@smartlog.get("/operacoes/{id_operacao}", response_model=Operacao)
async def read_empresa(id_operacao: int):
    if id_operacao < len(operacao_db):
        return operacao_db[id_operacao]
    raise HTTPException(status_code=404, detail="Operacao não encontrada")

@smartlog.put("/operacoes/{id_operacao}", response_model=Operacao)
async def update_empresa(id_operacao: int, updated_operacao: Operacao):
    if id_operacao < len(operacao_db):
        empresas_db[id_operacao] = updated_operacao
        return updated_operacao
    raise HTTPException(status_code=404, detail="Operacao não encontrada")

@smartlog.delete("/operacoes/{id_operacao}", response_model=Operacao)
async def delete_operacao(id_operacao: int):
    if id_operacao < len(operacao_db):
        delete_operacao = permissoes_db.pop(id_operacao)
        return delete_operacao
    raise HTTPException(status_code=404, detail="Operação não encontrada")