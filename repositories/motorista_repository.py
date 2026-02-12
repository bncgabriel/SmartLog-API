from sqlalchemy.orm import Session

from models.motorista_empresa import MotoristaEmpresa
from repositories.base import BaseRepository


class MotoristaRepository(BaseRepository[MotoristaEmpresa]):
    def __init__(self, db: Session):
        super().__init__(db, MotoristaEmpresa)

    def get_by_id(self, motorista_id: int) -> MotoristaEmpresa | None:
        return self.first_by(id_motorista_empresa=motorista_id)
