class DomainError(Exception):
    """Base para erros de domínio."""


class NotFoundError(DomainError):
    def __init__(self, entity: str, identifier: object, detail: str | None = None):
        self.entity = entity
        self.identifier = identifier
        self.detail = detail or f"{entity} não encontrado"
        super().__init__(self.detail)


class BusinessRuleError(DomainError):
    def __init__(self, detail: str):
        self.detail = detail
        super().__init__(detail)
