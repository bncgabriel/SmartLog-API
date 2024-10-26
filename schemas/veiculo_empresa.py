from pydantic import BaseModel

class VeiculoEmpresaBase(BaseModel):
    placa_cavalo: str
    placa_carreta: str

class VeiculoEmpresaCreate(VeiculoEmpresaBase):
    id_empresa: int
    id_motorista_vinculado: int

class VeiculoEmpresaRead(VeiculoEmpresaBase):
    id_veiculo: int

    class Config:
        orm_mode = True

class VeiculoEmpresaUpdate(VeiculoEmpresaBase):
    pass