from sqlalchemy.orm import Session

from models.veiculo_empresa import VeiculoEmpresa
from repositories.veiculo_repository import VeiculoRepository
from services.base import CrudService


class VeiculoService(CrudService[VeiculoEmpresa, str]):
    def __init__(self, db: Session, repository: VeiculoRepository):
        super().__init__(db, repository, "Veículo")
