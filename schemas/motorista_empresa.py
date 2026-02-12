from pydantic import BaseModel

class MotoristaEmpresaBase(BaseModel):
    nome_completo: str
    cpf: str
    rg: str
    telefone: str
    id_empresa: int

class MotoristaEmpresaCreate(MotoristaEmpresaBase):
    pass

class MotoristaEmpresaRead(MotoristaEmpresaBase):
    id_motorista_empresa: int

    class Config:
        orm_mode = True

class MotoristaEmpresaUpdate(BaseModel):
    nome_completo: str | None = None
    cpf: str | None = None
    rg: str | None = None
    telefone: str | None = None
    id_empresa: int | None = None
