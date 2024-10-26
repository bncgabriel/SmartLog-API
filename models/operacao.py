from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

class Operacao(Base):
    __tablename__ = 'operacao'
    id_operacao = Column(Integer, primary_key=True)
    navio_operacao = Column(String(50), nullable=False)
    pais_orig = Column(String(40), nullable=False)
    tipo_carga = Column(String(20), nullable=False)
    pesagem_total = Column(Numeric, nullable=False)
    inicio = Column(TIMESTAMP, nullable=False)
    fim = Column(TIMESTAMP, nullable = True)
    
    cargas_descargas = relationship("CargaDescarga", back_populates="operacao_rel")