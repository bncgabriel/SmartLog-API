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

class FuncionarioUpdate(BaseModel):
    nome_fun: str | None = None
    cpf_fun: str | None = None
    endereco_fun: str | None = None
    telefone_fun: str | None = None
    email_fun: str | None = None
    id_empresa_vinculada: int | None = None
    id_permissao: int | None = None
