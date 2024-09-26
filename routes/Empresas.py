from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

smartlog = FastAPI()

class Empresa(BaseModel):
    razao_social: str
    nome_fantasia: str
    cnpj: str
    endereco: str
    ie: str
    telefone: str
    email: str
    descricao: str

empresas_db = []

@smartlog.post("/empresas/", response_model=Empresa)
async def create_empresa(empresa: Empresa):
    empresas_db.append(empresa)
    return empresa

@smartlog.get("/empresas/", response_model=List[Empresa])
async def read_empresas():
    return empresas_db

@smartlog.get("/empresas/{empresa_id}", response_model=Empresa)
async def read_empresa(empresa_id: int):
    if 0 <= empresa_id < len(empresas_db):
        return empresas_db[empresa_id]
    raise HTTPException(status_code=404, detail="Empresa não encontrada")

@smartlog.put("/empresas/{empresa_id}", response_model=Empresa)
async def update_empresa(empresa_id: int, updated_empresa: Empresa):
    if 0 <= empresa_id < len(empresas_db):
        empresas_db[empresa_id] = updated_empresa
        return updated_empresa
    raise HTTPException(status_code=404, detail="Empresa não encontrada")

@smartlog.delete("/empresas/{empresa_id}", response_model=Empresa)
async def delete_empresa(empresa_id: int):
    if 0 <= empresa_id < len(empresas_db):
        deleted_empresa = empresas_db.pop(empresa_id)
        return deleted_empresa
    raise HTTPException(status_code=404, detail="Empresa não encontrada")