from sqlalchemy.orm import Session

from models.carga_descarga import CargaDescarga
from repositories.base import BaseRepository


class CargaDescargaRepository(BaseRepository[CargaDescarga]):
    def __init__(self, db: Session):
        super().__init__(db, CargaDescarga)

    def get_by_id(self, carga_descarga_id: int) -> CargaDescarga | None:
        return self.first_by(id_carga_descarga=carga_descarga_id)
