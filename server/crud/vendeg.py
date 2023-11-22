from datetime import datetime, timedelta
from fastapi import HTTPException
from sqlalchemy import func, asc
from sqlalchemy.orm import Session
from models import (
    vendeg as model_vendeg,
    foglalas as model_foglalas
    )
from schemas import vendeg as schema_vendeg

def vendeg_create(vendeg: schema_vendeg.VendegCreate, db: Session):
    db_vendeg = model_vendeg.Vendeg(email=vendeg.email, nev=vendeg.nev, telefonszam=vendeg.telefonszam, szuletesi_datum=vendeg.szuletesi_datum)
    db.add(db_vendeg)
    db.commit()
    db.refresh(db_vendeg)
    return db_vendeg

def vendeg_list(db: Session):
    return db.query(model_vendeg.Vendeg).all()

def vendeg_delete(email: str, db: Session):
    db_vendeg = db.query(model_vendeg.Vendeg).filter(model_vendeg.Vendeg.email == email).first()
    if db_vendeg is None:
        raise HTTPException(status_code=404, detail="Nincs ilyen vendeg")
    db.delete(db_vendeg)
    db.commit()
    return db_vendeg

def vendeg_update(email: str, vendeg: schema_vendeg.VendegCreate, db: Session):
    db_vendeg = db.query(model_vendeg.Vendeg).filter(model_vendeg.Vendeg.email == email).first()
    if not db_vendeg:
        raise HTTPException(status_code=404, detail="Nincs ilyen vendeg")
    
    if vendeg.nev is not None:
        db_vendeg.nev = vendeg.nev
    if vendeg.telefonszam is not None:
        db_vendeg.telefonszam = vendeg.telefonszam
    if vendeg.szuletesi_datum is not None:
        db_vendeg.szuletesi_datum = vendeg.szuletesi_datum
    
    db.commit()
    return db_vendeg

def fizetett_osszeg_legidosebb_vendeg(db: Session):
    legidosebb_vendeg = (
        db.query(model_vendeg.Vendeg)
        .order_by(asc(model_vendeg.Vendeg.szuletesi_datum))
        .first()
    )

    osszegzett_fizetesek = (
        db.query(func.sum(model_foglalas.Foglalas.fizetendo).label("osszeg"))
        .filter(model_foglalas.Foglalas.email == legidosebb_vendeg.email)
        .scalar() or 0
    )
    legidosebb_dict = legidosebb_vendeg.__dict__
    legidosebb_dict["osszeg"] = osszegzett_fizetesek

    return legidosebb_dict
