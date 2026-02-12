from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.motorista_empresa import MotoristaEmpresa
from schemas.motorista_empresa import MotoristaEmpresaCreate, MotoristaEmpresaRead, MotoristaEmpresaUpdate
from database import get_db

router = APIRouter()

@router.post("/", response_model=MotoristaEmpresaRead)
def create_motorista(motorista: MotoristaEmpresaCreate, db: Session = Depends(get_db)):
    db_motorista = MotoristaEmpresa(**motorista.dict())
    db.add(db_motorista)
    db.commit()
    db.refresh(db_motorista)
    return db_motorista

@router.get("/{motorista_id}", response_model=MotoristaEmpresaRead)
def buscar_motorista(motorista_id: int, db: Session = Depends(get_db)):
    db_motorista = db.query(MotoristaEmpresa).filter(MotoristaEmpresa.id_motorista_empresa == motorista_id).first()
    if db_motorista is None:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    return db_motorista

@router.put("/{motorista_id}", response_model=MotoristaEmpresaRead)
def atualizar_motorista(motorista_id: int, motorista: MotoristaEmpresaUpdate, db: Session = Depends(get_db)):
    db_motorista = db.query(MotoristaEmpresa).filter(MotoristaEmpresa.id_motorista_empresa == motorista_id).first()
    if db_motorista is None:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    for campo, valor in motorista.dict(exclude_unset=True).items():
        setattr(db_motorista, campo, valor)
    db.commit()
    db.refresh(db_motorista)
    return db_motorista

@router.delete("/{motorista_id}", response_model=MotoristaEmpresaRead)
def excluir_motorista(motorista_id: int, db: Session = Depends(get_db)):
    db_motorista = db.query(MotoristaEmpresa).filter(MotoristaEmpresa.id_motorista_empresa == motorista_id).first()
    if db_motorista is None:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    db.delete(db_motorista)
    db.commit()
    return db_motorista
