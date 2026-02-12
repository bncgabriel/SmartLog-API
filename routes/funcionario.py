from fastapi import APIRouter, Depends

from dependencies import get_funcionario_service
from schemas.funcionario import FuncionarioCreate, FuncionarioRead, FuncionarioUpdate
from services.funcionario_service import FuncionarioService

router = APIRouter()


@router.post("/", response_model=FuncionarioRead)
def cadastrar_funcionario(
    funcionario: FuncionarioCreate,
    service: FuncionarioService = Depends(get_funcionario_service),
):
    return service.create(funcionario.dict())


@router.get("/{funcionario_id}", response_model=FuncionarioRead)
def buscar_funcionario(
    funcionario_id: int,
    service: FuncionarioService = Depends(get_funcionario_service),
):
    return service.get_by_id(funcionario_id)


@router.get("/empresas/{id_empresa_vinculada}", response_model=list[FuncionarioRead])
def listar_funcionarios_por_empresa(
    id_empresa_vinculada: int,
    service: FuncionarioService = Depends(get_funcionario_service),
):
    return service.list_by_empresa(id_empresa_vinculada)


@router.put("/{funcionario_id}", response_model=FuncionarioRead)
def atualizar_funcionario(
    funcionario_id: int,
    funcionario: FuncionarioUpdate,
    service: FuncionarioService = Depends(get_funcionario_service),
):
    return service.update(funcionario_id, funcionario.dict(exclude_unset=True))


@router.delete("/{funcionario_id}", response_model=FuncionarioRead)
def excluir_funcionario(
    funcionario_id: int,
    service: FuncionarioService = Depends(get_funcionario_service),
):
    return service.delete(funcionario_id)
