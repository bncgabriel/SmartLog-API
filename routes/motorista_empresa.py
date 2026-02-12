from fastapi import APIRouter, Depends

from dependencies import get_motorista_service
from schemas.motorista_empresa import (
    MotoristaEmpresaCreate,
    MotoristaEmpresaRead,
    MotoristaEmpresaUpdate,
)
from services.motorista_service import MotoristaService

router = APIRouter()


@router.post("/", response_model=MotoristaEmpresaRead)
def create_motorista(
    motorista: MotoristaEmpresaCreate,
    service: MotoristaService = Depends(get_motorista_service),
):
    return service.create(motorista.dict())


@router.get("/{motorista_id}", response_model=MotoristaEmpresaRead)
def buscar_motorista(
    motorista_id: int,
    service: MotoristaService = Depends(get_motorista_service),
):
    return service.get_by_id(motorista_id)


@router.put("/{motorista_id}", response_model=MotoristaEmpresaRead)
def atualizar_motorista(
    motorista_id: int,
    motorista: MotoristaEmpresaUpdate,
    service: MotoristaService = Depends(get_motorista_service),
):
    return service.update(motorista_id, motorista.dict(exclude_unset=True))


@router.delete("/{motorista_id}", response_model=MotoristaEmpresaRead)
def excluir_motorista(
    motorista_id: int,
    service: MotoristaService = Depends(get_motorista_service),
):
    return service.delete(motorista_id)
