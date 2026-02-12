from sqlalchemy.orm import Session

from models.permissao import Permissao
from repositories.base import BaseRepository


class PermissaoRepository(BaseRepository[Permissao]):
    def __init__(self, db: Session):
        super().__init__(db, Permissao)

    def get_by_id(self, permissao_id: int) -> Permissao | None:
        return self.first_by(id_permissao=permissao_id)
