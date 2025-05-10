from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Role(Base):
    __tablename__ = 'role'

    id_role = Column(Integer, primary_key=True)
    role = Column(String(20), nullable=False)
    descricao_role = Column(String(50), nullable=False)

    funcionarios = relationship("Funcionario", back_populates="role")

    def update(self, data: dict):
           
            for key, value in data.items():
                if hasattr(self, key):
                    setattr(self, key, value)