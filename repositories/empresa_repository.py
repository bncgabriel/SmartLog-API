from sqlalchemy.orm import Session

from models.empresa import Empresa
from repositories.base import BaseRepository


class EmpresaRepository(BaseRepository[Empresa]):
    def __init__(self, db: Session):
        super().__init__(db, Empresa)

    def get_by_id(self, empresa_id: int) -> Empresa | None:
        return self.first_by(id_empresa=empresa_id)
