from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.empresa import Empresa
from schemas.empresa import EmpresaCreate, EmpresaRead, EmpresaUpdate
from database import get_db

router = APIRouter()

@router.post("/", response_model=EmpresaRead)
def cadastrar_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@router.get("/{empresa_id}", response_model=EmpresaRead)
def buscar_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id_empresa == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa not found")
    return db_empresa

@router.get("/", response_model=list[EmpresaRead])  
def listar_empresas (db: Session = Depends(get_db)):
    db_empresa = db.query(Empresa).all() 
    return db_empresa


@router.put("/{empresa_id}", response_model=EmpresaRead)
def atualizar_empresa (empresa_id: int, empresa: EmpresaUpdate, db: Session = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id_empresa == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa not found")
    for campo, valor in empresa.dict(exclude_unset=True).items():
        setattr(db_empresa, campo, valor)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@router.delete("/{empresa_id}", response_model=EmpresaRead)
def excluir_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id_empresa == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa not found")
    db.delete(db_empresa)
    db.commit()
    return db_empresa
