from sqlalchemy.orm import Session

from models.operacao import Operacao
from repositories.base import BaseRepository


class OperacaoRepository(BaseRepository[Operacao]):
    def __init__(self, db: Session):
        super().__init__(db, Operacao)

    def get_by_id(self, operacao_id: int) -> Operacao | None:
        return self.first_by(id_operacao=operacao_id)
