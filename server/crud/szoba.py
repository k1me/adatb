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


def szoba_delete(szobaszam: int, db: Session):
    db_szoba = (
        db.query(model_szoba.Szoba)
        .filter(model_szoba.Szoba.szobaszam == szobaszam)
        .first()
    )
    if db_szoba is None:
        raise HTTPException(status_code=404, detail="Nincs ilyen szoba")
    db.delete(db_szoba)
    db.commit()
    return db_szoba


def szoba_update(szobaszam: int, szoba: schema_szoba.SzobaCreate, db: Session):
    db_szoba = (
        db.query(model_szoba.Szoba)
        .filter(model_szoba.Szoba.szobaszam == szobaszam)
        .first()
    )
    if not db_szoba:
        raise HTTPException(status_code=404, detail="Nincs ilyen szoba")

    if szoba.megnevezes is not None:
        db_szoba.megnevezes = szoba.megnevezes

    db.commit()
    return db_szoba


# Listázza ki táblázatosan, hogy melyik típusú szobából hány darab van a szállodában!
def szobak_count_by_type(db: Session):
    db_szoba = db.query(model_szoba.Szoba).all()

    szobak = {}

    for szoba in db_szoba:
        if szoba.megnevezes in szobak:
            szobak[szoba.megnevezes] += 1
        else:
            szobak[szoba.megnevezes] = 1

    return szobak
