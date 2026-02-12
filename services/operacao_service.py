from sqlalchemy.orm import Session

from models.operacao import Operacao
from repositories.operacao_repository import OperacaoRepository
from services.base import CrudService


class OperacaoService(CrudService[Operacao, int]):
    def __init__(self, db: Session, repository: OperacaoRepository):
        super().__init__(db, repository, "Operação")
