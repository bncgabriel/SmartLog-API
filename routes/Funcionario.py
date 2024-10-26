from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.funcionario import Funcionario
from schemas.funcionario import FuncionarioCreate, FuncionarioRead, FuncionarioUpdate
from database import get_db

router = APIRouter()

@router.post("/", response_model=FuncionarioRead)
def cadastrar_funcionario(funcionario: FuncionarioCreate, db: Session = Depends(get_db)):
    db_funcionario = Funcionario(**funcionario.dict())
    db.add(db_funcionario)
    db.commit()
    db.refresh(db_funcionario)
    return db_funcionario


@router.get("/{funcionario_id}", response_model=FuncionarioRead)
def buscar_funcionario(funcionario_id: int, db: Session = Depends(get_db)):
    db_funcionario = db.query(Funcionario).filter(Funcionario.id_funcionario == funcionario_id).first()
    if db_funcionario is None:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return db_funcionario

@router.get("/empresas/{id_empresa_vinculada}", response_model=list[FuncionarioRead])
def listar_funcionarios_por_empresa(id_empresa_vinculada: int, db: Session = Depends(get_db)):
    db_funcionarios = db.query(Funcionario).filter(Funcionario.id_empresa_vinculada == id_empresa_vinculada).all()
    if not db_funcionarios:
        raise HTTPException(status_code=404, detail="Nenhum funcionário encontrado para esta empresa")
    return db_funcionarios


@router.put("/{funcionario_id}", response_model=FuncionarioRead)
def atualizar_funcionario(funcionario_id: int, funcionario: FuncionarioUpdate, db: Session = Depends(get_db)):
    db_funcionario = db.query(Funcionario).filter(Funcionario.id_funcionario == funcionario_id).first()
    if db_funcionario is None:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    for var, value in vars(funcionario).items():
        setattr(db_funcionario, var, value) if value else None
    db.commit()
    db.refresh(db_funcionario)
    return db_funcionario

@router.delete("/{funcionario_id}", response_model=FuncionarioRead)
def excluir_funcionario(funcionario_id: int, db: Session = Depends(get_db)):
    db_funcionario = db.query(Funcionario).filter(Funcionario.id_funcionario == funcionario_id).first()
    if db_funcionario is None:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    db.delete(db_funcionario)
    db.commit()
    return db_funcionario