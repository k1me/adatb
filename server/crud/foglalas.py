from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import foglalas as model_foglalas
from schemas import foglalas as schema_foglalas


def foglalas_create(foglalas: schema_foglalas.FoglalasCreate, db: Session):
    db_foglalas = model_foglalas.Foglalas(email=foglalas.email, mettol=foglalas.mettol, meddig=foglalas.meddig, fizetendo=foglalas.fizetendo)
    db.add(db_foglalas)
    db.commit()
    db.refresh(db_foglalas)
    return db_foglalas

def foglalas_list(db: Session):
    return db.query(model_foglalas.Foglalas).all()

def foglalas_delete(email: str, db: Session):
    db_foglalas = db.query(model_foglalas.Foglalas).filter(model_foglalas.Foglalas.email == email).first()
    if db_foglalas is None:
        raise HTTPException(status_code=404, detail="Nincs ilyen foglalas")
    db.delete(db_foglalas)
    db.commit()
    return db_foglalas

def foglalas_update(email: str, foglalas: schema_foglalas.FoglalasCreate, db: Session):
    db_foglalas = db.query(model_foglalas.Foglalas).filter(model_foglalas.Foglalas.email == email).first()
    if not db_foglalas:
        raise HTTPException(status_code=404, detail="Nincs ilyen foglalas")
    
    if foglalas.mettol is not None:
        db_foglalas.mettol = foglalas.mettol
    if foglalas.meddig is not None:
        db_foglalas.meddig = foglalas.meddig
    if foglalas.fizetendo is not None:
        db_foglalas.fizetendo = foglalas.fizetendo
    
    db.commit()
    return db_foglalas