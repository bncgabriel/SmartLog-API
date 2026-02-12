from sqlalchemy.orm import Session

from models.motorista_empresa import MotoristaEmpresa
from repositories.motorista_repository import MotoristaRepository
from services.base import CrudService


class MotoristaService(CrudService[MotoristaEmpresa, int]):
    def __init__(self, db: Session, repository: MotoristaRepository):
        super().__init__(db, repository, "Motorista")
