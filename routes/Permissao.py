from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

smartlog = FastAPI()

class Permissao(BaseModel):
    permissao: str
    descricao_permissao: str

permissoes_db = []

@smartlog.post("/permissoes/", response_model=Permissao)
async def criar_permissoes(permissao: Permissao):
    permissoes_db.append(permissao)
    return permissao

@smartlog.get("/permissoes/", response_model=List[Permissao])
async def read_permissoes():
    return permissoes_db

@smartlog.get("/permissoes/{permissao_id}", response_model=Permissao)
async def read_permissao(permissao_id: int):
    if permissao_id < len(permissoes_db):
        return permissoes_db[permissao_id]
    raise HTTPException(status_code=404, detail="Permissao não encontrada")

@smartlog.put("/permissoes/{permissao_id}", response_model=Permissao)
async def update_permissao(permissao_id: int, updated_permissao: Permissao):
    if permissao_id < len(permissoes_db):
        permissoes_db[permissao_id] = updated_permissao
        return updated_permissao
    raise HTTPException(status_code=404, detail="Permissao não encontrada")

@smartlog.delete("/permissoes/{permissao_id}", response_model=Permissao)
async def delete_permissao(permissao_id: int):
    if permissao_id < len(permissoes_db):
        deleted_permissao = permissoes_db.pop(permissao_id)
        return deleted_permissao
    raise HTTPException(status_code=404, detail="Permissao não encontrada")