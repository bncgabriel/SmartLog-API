from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from repositories.carga_descarga_repository import CargaDescargaRepository
from repositories.empresa_repository import EmpresaRepository
from repositories.funcionario_repository import FuncionarioRepository
from repositories.motorista_repository import MotoristaRepository
from repositories.operacao_repository import OperacaoRepository
from repositories.permissao_repository import PermissaoRepository
from repositories.veiculo_repository import VeiculoRepository
from services.carga_descarga_service import CargaDescargaService
from services.empresa_service import EmpresaService
from services.funcionario_service import FuncionarioService
from services.motorista_service import MotoristaService
from services.operacao_service import OperacaoService
from services.permissao_service import PermissaoService
from services.veiculo_service import VeiculoService


def get_empresa_service(db: Session = Depends(get_db)) -> EmpresaService:
    return EmpresaService(db, EmpresaRepository(db))


def get_permissao_service(db: Session = Depends(get_db)) -> PermissaoService:
    return PermissaoService(db, PermissaoRepository(db))


def get_funcionario_service(db: Session = Depends(get_db)) -> FuncionarioService:
    return FuncionarioService(db, FuncionarioRepository(db))


def get_motorista_service(db: Session = Depends(get_db)) -> MotoristaService:
    return MotoristaService(db, MotoristaRepository(db))


def get_veiculo_service(db: Session = Depends(get_db)) -> VeiculoService:
    return VeiculoService(db, VeiculoRepository(db))


def get_operacao_service(db: Session = Depends(get_db)) -> OperacaoService:
    return OperacaoService(db, OperacaoRepository(db))


def get_carga_descarga_service(db: Session = Depends(get_db)) -> CargaDescargaService:
    return CargaDescargaService(
        db,
        CargaDescargaRepository(db),
        OperacaoRepository(db),
    )
