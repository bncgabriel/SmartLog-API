from fastapi import APIRouter, Depends, status

from dependencies import get_permissao_service
from schemas.permissao import PermissaoCreate, PermissaoRead, PermissaoUpdate
from services.permissao_service import PermissaoService

router = APIRouter()


@router.post("/", response_model=PermissaoRead, status_code=status.HTTP_201_CREATED)
def criar_permissao(
    permissao: PermissaoCreate,
    service: PermissaoService = Depends(get_permissao_service),
):
    return service.create(permissao.dict())


@router.get("/", response_model=list[PermissaoRead])
def listar_permissoes(service: PermissaoService = Depends(get_permissao_service)):
    return service.list_all()


@router.get("/{permissao_id}", response_model=PermissaoRead)
def buscar_permissao(
    permissao_id: int,
    service: PermissaoService = Depends(get_permissao_service),
):
    return service.get_by_id(permissao_id)


@router.put("/{permissao_id}", response_model=PermissaoRead)
def atualizar_permissao(
    permissao_id: int,
    permissao: PermissaoUpdate,
    service: PermissaoService = Depends(get_permissao_service),
):
    return service.update(permissao_id, permissao.dict(exclude_unset=True))


@router.delete("/{permissao_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_permissao(
    permissao_id: int,
    service: PermissaoService = Depends(get_permissao_service),
):
    service.delete(permissao_id)
