from sqlalchemy import Column, DateTime, ForeignKey, ForeignKeyConstraint, Integer, String, Float, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import DATERANGE
from . import schem,models

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresa'
    id_empresa = Column(Integer, primary_key=True)
    razao_social = Column(String(100), nullable=False)
    nome_fantasia = Column(String(200), nullable=False)
    cnpj = Column(String(20), nullable=False, unique=True)
    endereco = Column(String(150), nullable=False)
    ie = Column(String(20), nullable=False, unique=True)
    telefone = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    descricao = Column(String(30))

class Permissao(Base):
    __tablename__ = 'permissao'
    id_permissao = Column(Integer, primary_key=True)
    permissao = Column(String(20), nullable=False)
    descricao_permissao = Column(String(100))

class Funcionario(Base):
    __tablename__ = 'funcionario'
    nome_fun = Column(String(200), nullable=False)
    cpf_fun = Column(String(15), nullable=False, unique=True)
    endereco_fun = Column(String(200), nullable=False)
    telefone_fun = Column(String(15), nullable=False)
    email_fun = Column(String(50))
    id_empresa_vinculada = Column(Integer, nullable=False)
    id_permissao = Column(Integer, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint([id_permissao], [Permissao.id_permissao]),
        ForeignKeyConstraint([id_empresa_vinculada], [Empresa.id_empresa])
    )

class MotoristaEmpresa(Base):
    __tablename__ = 'motorista_empresa'
    id_motorista_empresa = Column(Integer, primary_key=True)
    nome_completo = Column(String(255), nullable=False)
    cpf = Column(String(15), nullable=False, unique=True)
    rg = Column(String(20), nullable=False, unique=True)
    telefone = Column(String(20))
    id_empresa = Column(Integer)

    __table_args__ = (
        ForeignKeyConstraint([id_empresa], [Empresa.id_empresa]),
    )

class VeiculoEmpresa(Base):
    __tablename__ = 'veiculo_empresa'
    id_veiculo = Column(Integer, primary_key=True)
    placa_cavalo = Column(String(7), nullable=False, unique=True)
    placa_carreta = Column(String(7), nullable=False, unique=True)
    id_empresa = Column(Integer)
    id_motorista_vinculado = Column(Integer)

    __table_args__ = (
        ForeignKeyConstraint([id_empresa], [Empresa.id_empresa]),
        ForeignKeyConstraint([id_motorista_vinculado], [MotoristaEmpresa.id_motorista_empresa])
    )

class Operacao(Base):
    __tablename__ = 'operacao'
    id_operacao = Column(Integer, primary_key=True)
    navio_operacao = Column(String(50), nullable=False)
    pais_orig = Column(String(40), nullable=False)
    tipo_carga = Column(String(20), nullable=False)
    pesagem_total = Column(Numeric, nullable=False)
    periodo = Column(DATERANGE, nullable=False)

class CargaDescarga(Base):
    __tablename__ = 'carga_descarga'
    id_carga_descarga = Column(Integer, primary_key=True)
    data_hora_carga = Column(DateTime(timezone=True), nullable=False)
    pesagem = Column(Numeric, nullable=False)
    hora_saida = Column(DateTime(timezone=True), nullable=False)
    codigo_carga = Column(String(10), nullable=False)
    tag = Column(String(50))
    registro = Column(String(256))
    id_veiculo_empresa = Column(Integer, nullable=False)
    id_motorista_empresa = Column(Integer)
    operacao = Column(Integer, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint([id_veiculo_empresa], [VeiculoEmpresa.id_veiculo]),
        ForeignKeyConstraint([id_motorista_empresa], [MotoristaEmpresa.id_motorista_empresa]),
        ForeignKeyConstraint([operacao], [Operacao.id_operacao])
    )