from pydantic import BaseModel

class VeiculoEmpresaBase(BaseModel):
    placa_cavalo: str
    placa_carreta: str
    id_motorista_vinculado: int
    id_empresa: int

class VeiculoEmpresaCreate(VeiculoEmpresaBase):
    pass

class VeiculoEmpresaRead(VeiculoEmpresaBase):
    class Config:
        orm_mode = True

class VeiculoEmpresaUpdate(BaseModel):
    placa_cavalo: str | None = None
    placa_carreta: str | None = None
    id_motorista_vinculado: int | None = None
    id_empresa: int | None = None
