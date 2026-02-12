from sqlalchemy.orm import Session

from models.veiculo_empresa import VeiculoEmpresa
from repositories.base import BaseRepository


class VeiculoRepository(BaseRepository[VeiculoEmpresa]):
    def __init__(self, db: Session):
        super().__init__(db, VeiculoEmpresa)

    def get_by_id(self, placa_cavalo: str) -> VeiculoEmpresa | None:
        return self.first_by(placa_cavalo=placa_cavalo)
