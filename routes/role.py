from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.role import Role
from schemas.role import RoleCreate, RoleRead, RoleUpdate
from database import get_db

router = APIRouter()

@router.post("/", response_model=RoleRead, status_code=status.HTTP_201_CREATED)
def criar_role(role: RoleCreate, db: Session = Depends(get_db)):
    """Cria uma nova permissão."""
    db_role = Role(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

@router.get("/", response_model=list[RoleRead])  
def listar_role (db: Session = Depends(get_db)):
    db_role = db.query(Role).all() 
    return db_role

@router.get("/{role_id}", response_model=RoleRead)
def bucar_role(role_id: int, db: Session = Depends(get_db)) -> RoleRead:
    """Obtém uma permissão por ID."""
    db_role = db.get(Role, role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="Permissão não encontrada")
    return db_role

@router.put("/{role_id}", response_model=RoleRead)
def atualizar_role(role_id: int, role: RoleUpdate, db: Session = Depends(get_db)):
    """Atualiza uma permissão existente."""
    db_role = db.query(Role).filter(Role.id_role == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Permissão não encontrada")
    db_role.update(role.dict(exclude_unset=True))
    db.commit()
    db.refresh(db_role)
    return db_role

@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_role(role_id: int, db: Session = Depends(get_db)):
    """Deleta uma permissão."""
    db_role = db.query(Role).filter(Role.id_role == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Permissão não encontrada")

    db.delete(db_role)
    db.commit()