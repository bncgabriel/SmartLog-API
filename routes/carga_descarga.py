from fastapi import APIRouter, Depends

from dependencies import get_carga_descarga_service
from schemas.carga_descarga import CargaDescargaCreate, CargaDescargaRead, CargaDescargaUpdate
from services.carga_descarga_service import CargaDescargaService

router = APIRouter()


@router.post("/", response_model=CargaDescargaRead)
def criar_carga_descarga(
    carga_descarga: CargaDescargaCreate,
    service: CargaDescargaService = Depends(get_carga_descarga_service),
):
    return service.create(carga_descarga.dict())


@router.get("/{carga_descarga_id}", response_model=CargaDescargaRead)
def buscar_carga_descarga(
    carga_descarga_id: int,
    service: CargaDescargaService = Depends(get_carga_descarga_service),
):
    return service.get_by_id(carga_descarga_id)


@router.put("/{carga_descarga_id}", response_model=CargaDescargaRead)
def atualizar_carga_descarga(
    carga_descarga_id: int,
    carga_descarga: CargaDescargaUpdate,
    service: CargaDescargaService = Depends(get_carga_descarga_service),
):
    return service.update(carga_descarga_id, carga_descarga.dict(exclude_unset=True))


@router.delete("/{carga_descarga_id}", response_model=CargaDescargaRead)
def excluir_carga_descarga(
    carga_descarga_id: int,
    service: CargaDescargaService = Depends(get_carga_descarga_service),
):
    return service.delete(carga_descarga_id)
