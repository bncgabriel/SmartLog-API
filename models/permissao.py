from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Permissao(Base):
    __tablename__ = 'permissao'

    id_permissao = Column(Integer, primary_key=True)
    permissao = Column(String(20), nullable=False)
    descricao_permissao = Column(String(50), nullable=False)

    funcionarios = relationship("Funcionario", back_populates="permissao")

    def update(self, data: dict):
           
            for key, value in data.items():
                if hasattr(self, key):
                    setattr(self, key, value)