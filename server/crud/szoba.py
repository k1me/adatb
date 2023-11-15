from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import szoba as model_szoba
from schemas import szoba as schema_szoba


def szoba_create(szoba: schema_szoba.SzobaCreate, db: Session):
    db_szoba = model_szoba.Szoba(szobaszam=szoba.szobaszam, megnevezes=szoba.megnevezes)
    db.add(db_szoba)
    db.commit()
    db.refresh(db_szoba)
    return db_szoba

def szoba_list(db: Session):
    return db.query(model_szoba.Szoba).all()

def szoba_by_szobaszam(szobaszam: int, db: Session):
    db_szoba = db.query(model_szoba.Szoba).filter(model_szoba.Szoba.szobaszam == szobaszam).first()
    if db_szoba is None:
        raise HTTPException(status_code=404, detail="Nincs ilyen szoba")
    return db_szoba

def szoba_by_megnevezes(megnevezes: str, db: Session):
    db_szoba = db.query(model_szoba.Szoba).filter(model_szoba.Szoba.megnevezes == megnevezes).all()
    if not db_szoba:
        raise HTTPException(status_code=404, detail="Nincs ilyen szobatipus")
    return db_szoba
