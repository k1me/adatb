from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import kezeli as model_kezeli
from schemas import kezeli as schema_kezeli


def kezeli_create(kezeli: schema_kezeli.KezeliCreate, db: Session):
    db_kezeli = model_kezeli.Kezeli(
        felhasznalonev=kezeli.felhasznalonev,
        email=kezeli.email,
        mettol=kezeli.mettol,
        meddig=kezeli.meddig,
    )
    db.add(db_kezeli)
    db.commit()
    db.refresh(db_kezeli)
    return db_kezeli


def kezeli_list(db: Session):
    return db.query(model_kezeli.Kezeli).all()


def kezeli_by_felhasznalonev(felhasznalonev: str, db: Session):
    db_kezeli = (
        db.query(model_kezeli.Kezeli)
        .filter(model_kezeli.Kezeli.felhasznalonev == felhasznalonev)
        .all()
    )
    if not db_kezeli:
        raise HTTPException(status_code=404, detail="Nincs ilyen kezeli")
    return db_kezeli
