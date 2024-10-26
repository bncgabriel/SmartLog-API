from sqlalchemy import Column, DateTime, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TIMESTAMP
from database import Base

class CargaDescarga(Base):
    __tablename__ = 'carga_descarga'
    id_carga_descarga = Column(Integer, primary_key=True)
    data_hora_carga = Column(TIMESTAMP, nullable=False)
    pesagem = Column(Numeric, nullable=False)
    hora_saida = Column(TIMESTAMP, nullable=False)
    codigo_carga = Column(String(10), nullable=False)
    tag = Column(String(50))
    registro = Column(String(256))
    id_veiculo_empresa = Column(Integer, ForeignKey('veiculo_empresa.id_veiculo'), nullable=False)
    id_motorista_empresa = Column(Integer, ForeignKey('motorista_empresa.id_motorista_empresa'))
    operacao = Column(Integer, ForeignKey('operacao.id_operacao'), nullable=False)
    
    veiculo = relationship("VeiculoEmpresa", back_populates="cargas_descargas")
    motorista = relationship("MotoristaEmpresa", back_populates="cargas_descargas")
    operacao_rel = relationship("Operacao", back_populates="cargas_descargas")