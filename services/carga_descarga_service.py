from sqlalchemy.orm import Session

from core.errors import BusinessRuleError, NotFoundError
from models.carga_descarga import CargaDescarga
from repositories.carga_descarga_repository import CargaDescargaRepository
from repositories.operacao_repository import OperacaoRepository
from services.base import CrudService


class CargaDescargaService(CrudService[CargaDescarga, int]):
    def __init__(
        self,
        db: Session,
        repository: CargaDescargaRepository,
        operacao_repository: OperacaoRepository,
    ):
        super().__init__(db, repository, "Carga")
        self.repository = repository
        self.operacao_repository = operacao_repository

    def create(self, data: dict) -> CargaDescarga:
        operacao_id = data["operacao"]
        operacao = self.operacao_repository.get_by_id(operacao_id)
        if operacao is None:
            raise NotFoundError("Operação", operacao_id)

        pesagem = data["pesagem"]
        if pesagem > operacao.pesagem_total:
            raise BusinessRuleError("Peso da carga excede a pesagem total da operação")

        operacao.pesagem_total -= pesagem
        carga_descarga = self.repository.add(data)
        self.db.commit()
        self.db.refresh(carga_descarga)
        self.db.refresh(operacao)
        return carga_descarga
