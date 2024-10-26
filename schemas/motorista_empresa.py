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

class MotoristaEmpresaUpdate(MotoristaEmpresaBase):
    pass