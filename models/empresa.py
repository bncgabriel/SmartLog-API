from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = 'empresa'

    id_empresa = Column(Integer, primary_key=True, index=True)
    razao_social = Column(String(100), nullable=False)
    nome_fantasia = Column(String(200), nullable=False)
    cnpj = Column(String(20), nullable=False, unique=True)
    endereco = Column(String(150), nullable=False)
    ie = Column(String(20), nullable=False, unique=True)
    telefone = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    descricao = Column(String(30))


    funcionarios = relationship("Funcionario", back_populates="empresa")
    motoristas = relationship("MotoristaEmpresa", back_populates="empresa")
    veiculos = relationship("VeiculoEmpresa", back_populates="empresa")