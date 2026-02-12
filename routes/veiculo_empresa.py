from fastapi import APIRouter, Depends

from dependencies import get_veiculo_service
from schemas.veiculo_empresa import VeiculoEmpresaCreate, VeiculoEmpresaRead, VeiculoEmpresaUpdate
from services.veiculo_service import VeiculoService

router = APIRouter()


@router.post("/", response_model=VeiculoEmpresaRead)
def criar_veiculo(
    veiculo: VeiculoEmpresaCreate,
    service: VeiculoService = Depends(get_veiculo_service),
):
    return service.create(veiculo.dict())


@router.get("/{placa_cavalo}", response_model=VeiculoEmpresaRead)
def buscar_veiculo(
    placa_cavalo: str,
    service: VeiculoService = Depends(get_veiculo_service),
):
    return service.get_by_id(placa_cavalo)


@router.put("/{placa_cavalo}", response_model=VeiculoEmpresaRead)
def atualizar_veiculo(
    placa_cavalo: str,
    veiculo: VeiculoEmpresaUpdate,
    service: VeiculoService = Depends(get_veiculo_service),
):
    return service.update(placa_cavalo, veiculo.dict(exclude_unset=True))


@router.delete("/{placa_cavalo}", response_model=VeiculoEmpresaRead)
def excluir_veiculo(
    placa_cavalo: str,
    service: VeiculoService = Depends(get_veiculo_service),
):
    return service.delete(placa_cavalo)
