from datetime import datetime
from pydantic import BaseModel

class OperacaoBase(BaseModel):
    navio_operacao: str
    pais_orig: str
    tipo_carga: str
    pesagem_total: float 

class OperacaoCreate(OperacaoBase):
    inicio: datetime

class OperacaoRead(OperacaoBase):
    id_operacao: int
    inicio: datetime
    fim: datetime | None = None

    class Config:
        orm_mode = True

class OperacaoUpdate(BaseModel):
    navio_operacao: str | None = None
    pais_orig: str | None = None
    tipo_carga: str | None = None
    pesagem_total: float | None = None
    inicio: datetime | None = None
    fim: datetime | None = None
