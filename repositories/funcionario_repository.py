from sqlalchemy.orm import Session

from models.funcionario import Funcionario
from repositories.base import BaseRepository


class FuncionarioRepository(BaseRepository[Funcionario]):
    def __init__(self, db: Session):
        super().__init__(db, Funcionario)

    def get_by_id(self, funcionario_id: int) -> Funcionario | None:
        return self.first_by(id_funcionario=funcionario_id)

    def list_by_empresa(self, empresa_id: int) -> list[Funcionario]:
        return self.db.query(Funcionario).filter(Funcionario.id_empresa_vinculada == empresa_id).all()
