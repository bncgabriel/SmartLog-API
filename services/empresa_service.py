from sqlalchemy.orm import Session

from models.empresa import Empresa
from repositories.empresa_repository import EmpresaRepository
from services.base import CrudService


class EmpresaService(CrudService[Empresa, int]):
    def __init__(self, db: Session, repository: EmpresaRepository):
        super().__init__(db, repository, "Empresa")
