from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import szobatipus as model_szobatipus
from schemas import szobatipus as schema_szobatipus


def szobatipus_create(szobatipus: schema_szobatipus.SzobaTipusCreate, db: Session):
    db_szobatipus = model_szobatipus.SzobaTipus(megnevezes=szobatipus.megnevezes, napi_ar=szobatipus.napi_ar, fekvohelyek_szama=szobatipus.fekvohelyek_szama, leiras=szobatipus.leiras)
    db.add(db_szobatipus)
    db.commit()
    db.refresh(db_szobatipus)
    return db_szobatipus

def szobatipus_list(db: Session):
    return db.query(model_szobatipus.SzobaTipus).all()

def szobatipus_by_megnevezes(megnevezes: str, db: Session):
    db_szobatipus = db.query(model_szobatipus.SzobaTipus).filter(model_szobatipus.SzobaTipus.megnevezes == megnevezes).first()
    if db_szobatipus is None:
        raise HTTPException(status_code=404, detail="Nincs ilyen szobatipus")
    return db_szobatipus

def szobatipus_delete(megnevezes: str, db: Session):
    db_szobatipus = db.query(model_szobatipus.SzobaTipus).filter(model_szobatipus.SzobaTipus.megnevezes == megnevezes).first()
    if db_szobatipus is None:
        raise HTTPException(status_code=404, detail="Nincs ilyen szobatipus")
    db.delete(db_szobatipus)
    db.commit()
    return db_szobatipus

def szobatipus_update(megnevezes: str, szobatipus: schema_szobatipus.SzobaTipusCreate, db: Session):
    db_szobatipus = db.query(model_szobatipus.SzobaTipus).filter(model_szobatipus.SzobaTipus.megnevezes == megnevezes).first()
    if not db_szobatipus:
        raise HTTPException(status_code=404, detail="Nincs ilyen szobatipus")
    
    if szobatipus.napi_ar is not None:
        db_szobatipus.napi_ar = szobatipus.napi_ar
    
    db.commit()
    return db_szobatipus