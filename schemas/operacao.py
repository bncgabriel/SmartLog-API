from datetime import datetime
from pydantic import BaseModel, Field

class OperacaoBase(BaseModel):
    navio_operacao: str
    pais_orig: str
    tipo_carga: str
    pesagem_total: float 

class OperacaoCreate(OperacaoBase):
    inicio: datetime
    fim: datetime


    def validate_data(self):
        if self.fim <= self.inicio:
            raise ValueError("A data de fim deve ser posterior à data de início.")

class OperacaoRead(OperacaoBase):
    id_operacao: int

    class Config:
        orm_mode = True

class OperacaoUpdate(OperacaoBase):
    pass 