from typing import Any, Generic, TypeVar

from sqlalchemy.orm import Session

ModelT = TypeVar("ModelT")


class BaseRepository(Generic[ModelT]):
    def __init__(self, db: Session, model: type[ModelT]):
        self.db = db
        self.model = model

    def add(self, data: dict[str, Any]) -> ModelT:
        entity = self.model(**data)
        self.db.add(entity)
        return entity

    def list_all(self) -> list[ModelT]:
        return self.db.query(self.model).all()

    def first_by(self, **filters: Any) -> ModelT | None:
        return self.db.query(self.model).filter_by(**filters).first()

    def update_instance(self, entity: ModelT, data: dict[str, Any]) -> ModelT:
        for key, value in data.items():
            setattr(entity, key, value)
        return entity

    def delete_instance(self, entity: ModelT) -> None:
        self.db.delete(entity)
