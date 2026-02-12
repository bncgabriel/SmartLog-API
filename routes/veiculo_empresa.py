from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.veiculo_empresa import VeiculoEmpresa
from schemas.veiculo_empresa import VeiculoEmpresaCreate, VeiculoEmpresaRead, VeiculoEmpresaUpdate
from database import get_db

router = APIRouter()

@router.post("/", response_model=VeiculoEmpresaRead)
def criar_veiculo(veiculo: VeiculoEmpresaCreate, db: Session = Depends(get_db)):
    db_veiculo = VeiculoEmpresa(**veiculo.dict())
    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

@router.get("/{placa_cavalo}", response_model=VeiculoEmpresaRead)
def buscar_veiculo(placa_cavalo: str, db: Session = Depends(get_db)):
    db_veiculo = db.query(VeiculoEmpresa).filter(VeiculoEmpresa.placa_cavalo == placa_cavalo).first()
    if db_veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return db_veiculo

@router.put("/{placa_cavalo}", response_model=VeiculoEmpresaRead)
def atualizar_veiculo(placa_cavalo: str, veiculo: VeiculoEmpresaUpdate, db: Session = Depends(get_db)):
    db_veiculo = db.query(VeiculoEmpresa).filter(VeiculoEmpresa.placa_cavalo == placa_cavalo).first()
    if db_veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    for campo, valor in veiculo.dict(exclude_unset=True).items():
        setattr(db_veiculo, campo, valor)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

@router.delete("/{placa_cavalo}", response_model=VeiculoEmpresaRead)
def excluir_veiculo(placa_cavalo: str, db: Session = Depends(get_db)):
    db_veiculo = db.query(VeiculoEmpresa).filter(VeiculoEmpresa.placa_cavalo == placa_cavalo).first()
    if db_veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    db.delete(db_veiculo)
    db.commit()
    return db_veiculo
