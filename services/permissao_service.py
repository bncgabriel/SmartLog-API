from sqlalchemy.orm import Session

from models.permissao import Permissao
from repositories.permissao_repository import PermissaoRepository
from services.base import CrudService


class PermissaoService(CrudService[Permissao, int]):
    def __init__(self, db: Session, repository: PermissaoRepository):
        super().__init__(db, repository, "Permissão")
