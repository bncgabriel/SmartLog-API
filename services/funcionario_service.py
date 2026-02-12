from sqlalchemy.orm import Session

from core.errors import NotFoundError
from models.funcionario import Funcionario
from repositories.funcionario_repository import FuncionarioRepository
from services.base import CrudService


class FuncionarioService(CrudService[Funcionario, int]):
    def __init__(self, db: Session, repository: FuncionarioRepository):
        super().__init__(db, repository, "Funcionário")
        self.repository = repository

    def list_by_empresa(self, empresa_id: int) -> list[Funcionario]:
        funcionarios = self.repository.list_by_empresa(empresa_id)
        if not funcionarios:
            raise NotFoundError(
                "Funcionário",
                empresa_id,
                detail="Nenhum funcionário encontrado para esta empresa",
            )
        return funcionarios
