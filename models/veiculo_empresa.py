from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class VeiculoEmpresa(Base):
    __tablename__ = 'veiculo_empresa'
    id_veiculo = Column(Integer, primary_key=True)
    placa_cavalo = Column(String(7), nullable=False, unique=True)
    placa_carreta = Column(String(7), nullable=False, unique=True)
    id_empresa = Column(Integer, ForeignKey('empresa.id_empresa'))
    id_motorista_vinculado = Column(Integer, ForeignKey('motorista_empresa.id_motorista_empresa'))
    
    empresa = relationship("Empresa", back_populates="veiculos")
    motorista = relationship("MotoristaEmpresa", back_populates="veiculos")
    cargas_descargas = relationship("CargaDescarga", back_populates="veiculo")