from fastapi import APIRouter, Depends

from dependencies import get_operacao_service
from schemas.operacao import OperacaoCreate, OperacaoRead, OperacaoUpdate
from services.operacao_service import OperacaoService

router = APIRouter()


@router.post("/", response_model=OperacaoRead)
def criar_operacao(
    operacao: OperacaoCreate,
    service: OperacaoService = Depends(get_operacao_service),
):
    return service.create(operacao.dict())


@router.get("/{operacao_id}", response_model=OperacaoRead)
def buscar_operacao(
    operacao_id: int,
    service: OperacaoService = Depends(get_operacao_service),
):
    return service.get_by_id(operacao_id)


@router.get("/", response_model=list[OperacaoRead])
def listar_operacoes(service: OperacaoService = Depends(get_operacao_service)):
    return service.list_all()


@router.put("/{operacao_id}", response_model=OperacaoRead)
def atualizar_operacao(
    operacao_id: int,
    operacao: OperacaoUpdate,
    service: OperacaoService = Depends(get_operacao_service),
):
    return service.update(operacao_id, operacao.dict(exclude_unset=True))


@router.delete("/{operacao_id}", response_model=OperacaoRead)
def excluir_operacao(
    operacao_id: int,
    service: OperacaoService = Depends(get_operacao_service),
):
    return service.delete(operacao_id)
