# schemas/carga_descarga.py
from pydantic import BaseModel

class CargaDescargaBase(BaseModel):
    data_hora_carga: str
    pesagem: float
    hora_saida: str
    codigo_carga: str
    tag: str
    registro: str

class CargaDescargaCreate(CargaDescargaBase):
    id_veiculo_empresa: int
    id_motorista_empresa: int
    operacao: int

class CargaDescargaRead(CargaDescargaBase):
    id_carga_descarga: int

    class Config:
        orm_mode = True

class CargaDescargaUpdate(CargaDescargaBase):
    pass