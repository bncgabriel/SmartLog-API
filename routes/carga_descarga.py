from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.carga_descarga import CargaDescarga
from schemas.carga_descarga import CargaDescargaCreate, CargaDescargaRead, CargaDescargaUpdate
from database import get_db

router = APIRouter()

@router.post("/", response_model=CargaDescargaRead)
def criar_carga_descarga(carga_descarga: CargaDescargaCreate, db: Session = Depends(get_db)):
    db_carga_descarga = CargaDescarga(**carga_descarga.dict())
    db.add(db_carga_descarga)
    db.commit()
    db.refresh(db_carga_descarga)
    return db_carga_descarga

@router.get("/{carga_descarga_id}", response_model=CargaDescargaRead)
def buscar_carga_descarga(carga_descarga_id: int, db: Session = Depends(get_db)):
    db_carga_descarga = db.query(CargaDescarga).filter(CargaDescarga.id_carga_descarga == carga_descarga_id).first()
    if db_carga_descarga is None:
        raise HTTPException(status_code=404, detail="Carga não encontrada")
    return db_carga_descarga

@router.put("/{carga_descarga_id}", response_model=CargaDescargaRead)
def atualizar_carga_descarga(carga_descarga_id: int, carga_descarga: CargaDescargaUpdate, db: Session = Depends(get_db)):
    db_carga_descarga = db.query(CargaDescarga).filter(CargaDescarga.id_carga_descarga == carga_descarga_id).first()
    if db_carga_descarga is None:
        raise HTTPException(status_code=404, detail="Carga não encontrada")
    for var, value in vars(carga_descarga).items():
        setattr(db_carga_descarga, var, value) if value else None
    db.commit()
    db.refresh(db_carga_descarga)
    return db_carga_descarga

@router.delete("/{carga_descarga_id}", response_model=CargaDescargaRead)
def excluir_carga_descarga(carga_descarga_id: int, db: Session = Depends(get_db)):
    db_carga_descarga = db.query(CargaDescarga).filter(CargaDescarga.id_carga_descarga == carga_descarga_id).first()
    if db_carga_descarga is None:
        raise HTTPException(status_code=404, detail="Carga não encontrada")
    db.delete(db_carga_descarga)
    db.commit()
    return db_carga_descarga