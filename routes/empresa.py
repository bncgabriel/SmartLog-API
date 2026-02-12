from fastapi import APIRouter, Depends

from dependencies import get_empresa_service
from schemas.empresa import EmpresaCreate, EmpresaRead, EmpresaUpdate
from services.empresa_service import EmpresaService

router = APIRouter()


@router.post("/", response_model=EmpresaRead)
def cadastrar_empresa(
    empresa: EmpresaCreate,
    service: EmpresaService = Depends(get_empresa_service),
):
    return service.create(empresa.dict())


@router.get("/{empresa_id}", response_model=EmpresaRead)
def buscar_empresa(
    empresa_id: int,
    service: EmpresaService = Depends(get_empresa_service),
):
    return service.get_by_id(empresa_id)


@router.get("/", response_model=list[EmpresaRead])
def listar_empresas(service: EmpresaService = Depends(get_empresa_service)):
    return service.list_all()


@router.put("/{empresa_id}", response_model=EmpresaRead)
def atualizar_empresa(
    empresa_id: int,
    empresa: EmpresaUpdate,
    service: EmpresaService = Depends(get_empresa_service),
):
    return service.update(empresa_id, empresa.dict(exclude_unset=True))


@router.delete("/{empresa_id}", response_model=EmpresaRead)
def excluir_empresa(
    empresa_id: int,
    service: EmpresaService = Depends(get_empresa_service),
):
    return service.delete(empresa_id)
