from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.operacao import Operacao
from schemas.operacao import OperacaoCreate, OperacaoRead, OperacaoUpdate
from database import get_db

router = APIRouter()

@router.post("/", response_model=OperacaoRead)
def criar_operacao(operacao: OperacaoCreate, db: Session = Depends(get_db)):
    db_operacao = Operacao(**operacao.dict())
    db.add(db_operacao)
    db.commit()
    db.refresh(db_operacao)
    return db_operacao

@router.get("/{operacao_id}", response_model=OperacaoRead)
def buscar_operacao(operacao_id: int, db: Session = Depends(get_db)):
    db_operacao = db.query(Operacao).filter(Operacao.id_operacao == operacao_id).first()
    if db_operacao is None:
        raise HTTPException(status_code=404, detail="Operação não encontrada")
    return db_operacao

@router.get("/", response_model=list[OperacaoRead])  
def listar_operacoes (db: Session = Depends(get_db)):
    db_operacao = db.query(Operacao).all() 
    return db_operacao

@router.put("/{operacao_id}", response_model=OperacaoRead)
def atualizar_operacao(operacao_id: int, operacao: OperacaoUpdate, db: Session = Depends(get_db)):
    db_operacao = db.query(Operacao).filter(Operacao.id_operacao == operacao_id).first()
    if db_operacao is None:
        raise HTTPException(status_code=404, detail="Operação não encontrada")
    for var, value in vars(operacao).items():
        setattr(db_operacao, var, value) if value else None
    db.commit()
    db.refresh(db_operacao)
    return db_operacao

@router.delete("/{operacao_id}", response_model=OperacaoRead)
def excluir_operacao(operacao_id: int, db: Session = Depends(get_db)):
    db_operacao = db.query(Operacao).filter(Operacao.id_operacao == operacao_id).first()
    if db_operacao is None:
        raise HTTPException(status_code=404, detail="Operação não encontrada")
    db.delete(db_operacao)
    db.commit()
    return db_operacao