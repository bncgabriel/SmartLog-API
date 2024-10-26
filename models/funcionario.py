from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Funcionario(Base):
    __tablename__ = 'funcionario'

    id_funcionario = Column(Integer, primary_key=True)
    nome_fun = Column(String(200), nullable=False)
    cpf_fun = Column(String(15), nullable=False, unique=True)
    endereco_fun = Column(String(200), nullable=False)
    telefone_fun = Column(String(15), nullable=False)
    email_fun = Column(String(50))
    id_empresa_vinculada = Column(Integer, ForeignKey('empresa.id_empresa'), nullable=False)
    id_permissao = Column(Integer, ForeignKey('permissao.id_permissao'), nullable=False)

    empresa = relationship("Empresa", back_populates="funcionarios")
    permissao = relationship("Permissao", back_populates="funcionarios")
