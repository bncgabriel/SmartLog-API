from datetime import datetime
from pydantic import BaseModel

class CargaDescargaBase(BaseModel):
    codigo_carga: str
    tag: str
    registro: str

class CargaDescargaCreate(CargaDescargaBase):
    data_hora_carga: datetime
    pesagem: float
    hora_saida: datetime
    placa_veiculoc_empresa: str
    id_motorista_empresa: int
    operacao: int

class CargaDescargaRead(CargaDescargaBase):
    pesagem: float
    hora_saida: datetime
    hora_final: datetime
    placa_veiculoc_empresa: str
    id_motorista_empresa: int
    operacao: int
    id_carga_descarga: int

    class Config:
        orm_mode = True

class CargaDescargaUpdate(CargaDescargaBase):
    hora_final: datetime