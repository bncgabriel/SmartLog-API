from sqlalchemy import Column, DateTime, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TIMESTAMP
from database import Base

class CargaDescarga(Base):
    __tablename__ = 'carga_descarga'
    id_carga_descarga = Column(Integer, primary_key=True)
    pesagem = Column(Float, nullable=False)
    hora_saida = Column(TIMESTAMP, nullable=False)
    hora_final = Column(TIMESTAMP, nullable = True)
    codigo_carga = Column(String(10), nullable=False)
    tag = Column(String(50))
    registro = Column(String(256))
    placa_veiculoc_empresa = Column(String(7), ForeignKey('veiculo_empresa.placa_cavalo'), nullable=False)
    id_motorista_empresa = Column(Integer, ForeignKey('motorista_empresa.id_motorista_empresa'))
    operacao = Column(Integer, ForeignKey('operacao.id_operacao'), nullable=False)
    
    veiculos = relationship("VeiculoEmpresa", back_populates="cargas_descargas")
    motorista = relationship("MotoristaEmpresa", back_populates="cargas_descargas")
    operacao_rel = relationship("Operacao", back_populates="cargas_descargas")