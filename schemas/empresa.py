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

class EmpresaUpdate(EmpresaBase):
    pass
