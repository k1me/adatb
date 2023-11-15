from datetime import datetime, timedelta
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import vendeg as model_vendeg
from schemas import vendeg as schema_vendeg

def vendeg_create(vendeg: schema_vendeg.VendegCreate, db: Session):
    db_vendeg = model_vendeg.Vendeg(email=vendeg.email, nev=vendeg.nev, telefonszam=vendeg.telefonszam, szuletesi_datum=vendeg.szuletesi_datum)
    db.add(db_vendeg)
    db.commit()
    db.refresh(db_vendeg)
    return db_vendeg

def vendeg_list(db: Session):
    return db.query(model_vendeg.Vendeg).all()

def vendeg_by_email(email: str, db: Session):
    db_vendeg = db.query(model_vendeg.Vendeg).filter(model_vendeg.Vendeg.email == email).first()
    if db_vendeg is None:
        raise HTTPException(status_code=404, detail="Nincs ilyen vendeg")
    return db_vendeg

def vendeg_by_nev(nev: str, db: Session):
    db_vendeg = db.query(model_vendeg.Vendeg).filter(model_vendeg.Vendeg.nev == nev).all()
    if not db_vendeg:
        raise HTTPException(status_code=404, detail="Nincs ilyen vendeg")
    return db_vendeg

def vendeg_by_datum(datum: str, db: Session):
    try:
        datum_converted = datetime.strptime(datum, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Hibas datum")
    db_vendeg = db.query(model_vendeg.Vendeg).filter(model_vendeg.Vendeg.szuletesi_datum == datum_converted).all()
    if not db_vendeg:
        raise HTTPException(status_code=404, detail="Nincs ilyen vendeg")
    return db_vendeg

def vendeg_fiatalabb(ev: int, db: Session):
    db_vendeg = db.query(model_vendeg.Vendeg).filter(model_vendeg.Vendeg.szuletesi_datum > datetime.now() - timedelta(days=365*ev)).all()
    if not db_vendeg:
        raise HTTPException(status_code=404, detail="Nincs ilyen vendeg")
    return db_vendeg

def vendeg_idosebb(ev: int, db: Session):
    db_vendeg = db.query(model_vendeg.Vendeg).filter(model_vendeg.Vendeg.szuletesi_datum < datetime.now() - timedelta(days=365*ev)).all()
    if not db_vendeg:
        raise HTTPException(status_code=404, detail="Nincs ilyen vendeg")
    return db_vendeg
