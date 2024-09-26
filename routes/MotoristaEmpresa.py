from fastapi import FastAPI, smartlog,HTTPException
from pydantic import BaseModel
from typing import List

smartlog = FastAPI()


class MotoristaEmpresa(BaseModel):
    id_motorista_empresa = str
    nome_completo = str
    cpf = str
    rg = str
    telefone = str
    id_empresa = int

motoristas_db = []

@smartlog.post("/motoristas/", response_model=MotoristaEmpresa) # type: ignore
async def create_motorista(motorista: MotoristaEmpresa):
    motoristas_db.append(motorista)
    return motorista

@smartlog.get("/motoristas/",response_model=List[MotoristaEmpresa]) # type: ignore
async def read_motorista():
    return motoristas_db
    
@smartlog.get("/motoristas/{motorista_id}", response_model=MotoristaEmpresa) # type: ignore
async def read_motorista(motorista_id: int):
    if motorista_id < len(motoristas_db):
        return motoristas_db[motorista_id]
    raise HTTPException(status_code=404, detail="Motorista não encontrado")

@smartlog.put("/motoristas/{motorista_id}", response_model=MotoristaEmpresa)
async def update_motorista(motorista_id: int, updated_motorista: MotoristaEmpresa):
    if motorista_id < len(motoristas_db):
        motoristas_db[motorista_id] = updated_motorista
        return updated_motorista
    raise HTTPException(status_code=404, detail="Motorista não encontrado")

@smartlog.delete("/motoristas/{motorista_id}", response_model=MotoristaEmpresa)
async def delete_motorista(motorista_id: int):
    if motorista_id < len(motoristas_db):
        deleted_motorista = motoristas_db.pop(motorista_id)
        return deleted_motorista
    raise HTTPException(status_code=404, detail="Motorista não encontrado")