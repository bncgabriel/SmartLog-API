from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class MotoristaEmpresa(Base):
    __tablename__ = 'motorista_empresa'
    id_motorista_empresa = Column(Integer, primary_key=True)
    nome_completo = Column(String(255), nullable=False)
    cpf = Column(String(15), nullable=False, unique=True)
    rg = Column(String(9), nullable=False, unique=True)
    telefone = Column(String(20))
    id_empresa = Column(Integer, ForeignKey('empresa.id_empresa'), nullable=False)
    
    empresa = relationship("Empresa", back_populates="motoristas")
    veiculos = relationship("VeiculoEmpresa", back_populates="motorista")
    cargas_descargas = relationship("CargaDescarga", back_populates="motorista")
