from pydantic import BaseModel

class EmpresaBase(BaseModel):
    razao_social: str
    nome_fantasia: str
    cnpj: str
    endereco: str
    ie: str
    telefone: str
    email: str
    descricao: str

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaRead(EmpresaBase):
    id_empresa: int

    class Config:
        orm_mode = True

class EmpresaUpdate(BaseModel):
    razao_social: str | None = None
    nome_fantasia: str | None = None
    cnpj: str | None = None
    endereco: str | None = None
    ie: str | None = None
    telefone: str | None = None
    email: str | None = None
    descricao: str | None = None
