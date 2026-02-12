from typing import Any, Generic, TypeVar

from sqlalchemy.orm import Session

from core.errors import NotFoundError
from services.protocols import CrudRepositoryProtocol

ModelT = TypeVar("ModelT")
IdT = TypeVar("IdT")


class CrudService(Generic[ModelT, IdT]):
    def __init__(
        self,
        db: Session,
        repository: CrudRepositoryProtocol[ModelT, IdT],
        entity_label: str,
    ):
        self.db = db
        self.repository = repository
        self.entity_label = entity_label

    def create(self, data: dict[str, Any]) -> ModelT:
        entity = self.repository.add(data)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def list_all(self) -> list[ModelT]:
        return self.repository.list_all()

    def get_by_id(self, entity_id: IdT) -> ModelT:
        entity = self.repository.get_by_id(entity_id)
        if entity is None:
            raise NotFoundError(self.entity_label, entity_id)
        return entity

    def update(self, entity_id: IdT, data: dict[str, Any]) -> ModelT:
        entity = self.get_by_id(entity_id)
        self.repository.update_instance(entity, data)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def delete(self, entity_id: IdT) -> ModelT:
        entity = self.get_by_id(entity_id)
        self.repository.delete_instance(entity)
        self.db.commit()
        return entity
