from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.permissao import Permissao
from schemas.permissao import PermissaoCreate, PermissaoRead, PermissaoUpdate
from database import get_db

router = APIRouter()

@router.post("/", response_model=PermissaoRead, status_code=status.HTTP_201_CREATED)
def criar_permissao(permissao: PermissaoCreate, db: Session = Depends(get_db)):
    """Cria uma nova permissão."""
    db_permissao = Permissao(**permissao.dict())
    db.add(db_permissao)
    db.commit()
    db.refresh(db_permissao)
    return db_permissao

@router.get("/", response_model=list[PermissaoRead])  
def listar_permissao (db: Session = Depends(get_db)):
    db_permissao = db.query(Permissao).all() 
    return db_permissao

@router.get("/{permissao_id}", response_model=PermissaoRead)
def bucar_permissao(permissao_id: int, db: Session = Depends(get_db)) -> PermissaoRead:
    """Obtém uma permissão por ID."""
    db_permissao = db.get(Permissao, permissao_id)
    if not db_permissao:
        raise HTTPException(status_code=404, detail="Permissão não encontrada")
    return db_permissao

@router.put("/{permissao_id}", response_model=PermissaoRead)
def atualizar_permissao(permissao_id: int, permissao: PermissaoUpdate, db: Session = Depends(get_db)):
    """Atualiza uma permissão existente."""
    db_permissao = db.query(Permissao).filter(Permissao.id_permissao == permissao_id).first()
    if not db_permissao:
        raise HTTPException(status_code=404, detail="Permissão não encontrada")
    db_permissao.update(permissao.dict(exclude_unset=True))
    db.commit()
    db.refresh(db_permissao)
    return db_permissao

@router.delete("/{permissao_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_permissao(permissao_id: int, db: Session = Depends(get_db)):
    """Deleta uma permissão."""
    db_permissao = db.query(Permissao).filter(Permissao.id_permissao == permissao_id).first()
    if not db_permissao:
        raise HTTPException(status_code=404, detail="Permissão não encontrada")

    db.delete(db_permissao)
    db.commit()