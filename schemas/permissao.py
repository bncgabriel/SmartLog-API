from pydantic import BaseModel

class PermissaoBase(BaseModel):
    permissao: str
    descricao_permissao: str

class PermissaoCreate(PermissaoBase):
    pass

class PermissaoRead(PermissaoBase):
    id_permissao: int

    class Config:
        orm_mode = True

class PermissaoUpdate(BaseModel):
    permissao: str | None = None
    descricao_permissao: str | None = None
