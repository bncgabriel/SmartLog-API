from datetime import datetime
from pydantic import BaseModel

class CargaDescargaBase(BaseModel):
    codigo_carga: str
    tag: str | None = None
    registro: str | None = None

class CargaDescargaCreate(CargaDescargaBase):
    pesagem: float
    hora_saida: datetime
    placa_veiculoc_empresa: str
    id_motorista_empresa: int
    operacao: int

class CargaDescargaRead(CargaDescargaBase):
    id_carga_descarga: int
    pesagem: float
    hora_saida: datetime
    hora_final: datetime | None = None
    placa_veiculoc_empresa: str
    id_motorista_empresa: int
    operacao: int

    class Config:
        orm_mode = True

class CargaDescargaUpdate(BaseModel):
    codigo_carga: str | None = None
    tag: str | None = None
    registro: str | None = None
    hora_final: datetime | None = None
