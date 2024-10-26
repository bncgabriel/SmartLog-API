from pydantic import BaseModel

class FuncionarioBase(BaseModel):
    nome_fun: str
    cpf_fun: str
    endereco_fun: str
    telefone_fun: str
    email_fun: str
    id_empresa_vinculada: int
    id_permissao: int

class FuncionarioCreate(FuncionarioBase):
    pass

class FuncionarioRead(FuncionarioBase):
    id_funcionario: int

    class Config:
        orm_mode = True

class FuncionarioUpdate(FuncionarioBase):
    pass