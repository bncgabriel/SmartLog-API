from pydantic import BaseModel

class PermissaoBase(BaseModel):
    permissao: str
    descricao_permissao: str

class PermissaoCreate(PermissaoBase):
    permissao: str
    descricao_permissao: str

class PermissaoRead(PermissaoBase):
    id_permissao: int

    class Config:
        orm_mode = True

class PermissaoUpdate(PermissaoBase):
    pass