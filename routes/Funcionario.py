from fastapi import FastAPI, smartlog,HTTPException
from pydantic import BaseModel
from typing import List

from models import Permissao

smartlog = FastAPI()


class Funcionario(BaseModel):
    nome: str
    cpf: str
    rg: str
    endereco: str
    telefone: str
    email: str
    cargo: str
    salario: float
    data_contratacao: str


funcionario_db = [] 

@smartlog.post("/funcionarios/", response_model=Funcionario)
async def create_funcionario(funcionario: Funcionario):
    funcionario_db.append(funcionario)
    return funcionario

@smartlog.get("/funcionarios/", response_model=List[Funcionario])
async def read_funcionarios():
    return funcionario_db  ##Quando adicionei o método n aceitou funcionario no plural 

@smartlog.get("/funcionarios/{funcionario_id}", response_model=Funcionario)
async def read_funcionario(funcionario_id:int):
    if funcionario_id < len(funcionario_db):
        return funcionario_db[funcionario_id]
    raise HTTPException(status_code=404, detail="Funcionário não encontrada")

@smartlog.put("/funcionarios/{funcionario_id}",response_model=Permissao)
async def update_funcionario(funcionario_id: int, update_funcionario: Funcionario):
    if funcionario_id < len(funcionario_db):
        funcionario_db[funcionario_id] = update_funcionario
        return update_funcionario
    raise HTTPException(status_code=404, detail="Funcionário não econtrada")
    
@smartlog.delete("/funcionarios/{funcionario_id}", response_model= Funcionario)
async def delete_funcionario(funcionario_id: int):
    if funcionario_id < len(funcionario_db):
        delete_funcionario = funcionario_db.pop(funcionario_id)
        return delete_funcionario
    raise HTTPException(status_code=404, detail="Funcionário não encontrado")