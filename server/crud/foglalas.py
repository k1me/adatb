from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas import foglalas as schema_foglalas
from datetime import datetime
from models import (
    foglalas as model_foglalas,
    szobaja as model_szobaja,
    szobatipus as model_szobatipusa,
    szoba as model_szoba,
)


def foglalas_create(foglalas: schema_foglalas.FoglalasCreate, db: Session):
    db_foglalas = model_foglalas.Foglalas(
        email=foglalas.email,
        mettol=foglalas.mettol,
        meddig=foglalas.meddig,
        fizetendo=foglalas.fizetendo,
    )
    db.add(db_foglalas)
    db.commit()
    db.refresh(db_foglalas)
    return db_foglalas


def foglalas_list(db: Session):
    return db.query(model_foglalas.Foglalas).all()


def foglalas_delete(email: str, mettol: datetime, meddig: datetime, db: Session):
    db_foglalas = (
        db.query(model_foglalas.Foglalas)
        .filter(
            model_foglalas.Foglalas.email == email,
            model_foglalas.Foglalas.mettol == mettol,
            model_foglalas.Foglalas.meddig == meddig,
        )
        .first()
    )
    if db_foglalas is None:
        raise HTTPException(status_code=404, detail="Nincs ilyen foglalas")
    db.delete(db_foglalas)
    db.commit()
    return db_foglalas


def foglalas_update(email: str, foglalas: schema_foglalas.FoglalasCreate, db: Session):
    db_foglalas = (
        db.query(model_foglalas.Foglalas)
        .filter(model_foglalas.Foglalas.email == email)
        .first()
    )
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


# Listázza ki táblázatos formában azon foglalások adatait időrendi sorrendben,
# amelyek a legalább 3 fekvőhellyel rendelkező szobákra vonatkoznak!
def foglalas_filtered(db: Session):
    foglalasok = (
        db.query(
            model_szobaja.Szobaja,
            model_szobatipusa.SzobaTipus.megnevezes.label("szobatipus_megnevezes"),
        )
        .join(
            model_szoba.Szoba,
            model_szoba.Szoba.szobaszam == model_szobaja.Szobaja.szobaszam,
        )
        .join(
            model_szobatipusa.SzobaTipus,
            model_szobatipusa.SzobaTipus.megnevezes == model_szoba.Szoba.megnevezes,
        )
        .filter(model_szobatipusa.SzobaTipus.fekvohelyek_szama >= 3)
        .all()
    )

    foglalasok_formatted = []
    for foglalas in foglalasok:
        szobaja, szobatipus_megnevezes = foglalas
        foglalasok_formatted.append(
            {
                "email": szobaja.email,
                "szobaszam": szobaja.szobaszam,
                "mettol": szobaja.mettol,
                "meddig": szobaja.meddig,
                "megnevezes": szobatipus_megnevezes,
            }
        )
    foglalasok_formatted.sort(key=lambda foglalas: foglalas["mettol"])

    return foglalasok_formatted
