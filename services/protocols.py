from typing import Any, Protocol, TypeVar

ModelT = TypeVar("ModelT")
IdT = TypeVar("IdT")


class CrudRepositoryProtocol(Protocol[ModelT, IdT]):
    def add(self, data: dict[str, Any]) -> ModelT:
        ...

    def list_all(self) -> list[ModelT]:
        ...

    def get_by_id(self, entity_id: IdT) -> ModelT | None:
        ...

    def update_instance(self, entity: ModelT, data: dict[str, Any]) -> ModelT:
        ...

    def delete_instance(self, entity: ModelT) -> None:
        ...
