from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import felhasznalo as model_felhasznalo
from schemas import felhasznalo as schema_felhasznalo
from encrypt import hash_password
from passlib.hash import sha256_crypt


def felhasznalo_create(felhasznalo: schema_felhasznalo.FelhasznaloCreate, db: Session):
    db_felhasznalo = model_felhasznalo.Felhasznalo(
        felhasznalonev=felhasznalo.felhasznalonev,
        nev=felhasznalo.nev,
        jelszo=hash_password(felhasznalo.jelszo),
    )

    db.add(db_felhasznalo)
    db.commit()
    db.refresh(db_felhasznalo)

    return db_felhasznalo


def felhasznalo_list(db: Session):
    return db.query(model_felhasznalo.Felhasznalo).all()


def felhasznalo_delete(felhasznalonev: str, db: Session):
    db_felhasznalo = (
        db.query(model_felhasznalo.Felhasznalo)
        .filter(model_felhasznalo.Felhasznalo.felhasznalonev == felhasznalonev)
        .first()
    )

    if db_felhasznalo is None:
        raise HTTPException(status_code=404, detail="Nincs ilyen felhasznalo")

    db.delete(db_felhasznalo)
    db.commit()

    return db_felhasznalo


def felhasznalo_update(
    felhasznalonev: str, felhasznalo: schema_felhasznalo.FelhasznaloCreate, db: Session
):
    db_felhasznalo = (
        db.query(model_felhasznalo.Felhasznalo)
        .filter(model_felhasznalo.Felhasznalo.felhasznalonev == felhasznalonev)
        .first()
    )

    if not db_felhasznalo:
        raise HTTPException(status_code=404, detail="Nincs ilyen felhasznalo")

    if felhasznalo.nev is not None:
        db_felhasznalo.nev = felhasznalo.nev

    if felhasznalo.jelszo is not None:
        db_felhasznalo.jelszo = felhasznalo.jelszo

    db.commit()

    return db_felhasznalo


def felhasznalo_login(felhasznalo: schema_felhasznalo.Bejelentkezes, db: Session):
    db_felhasznalo = (
        db.query(model_felhasznalo.Felhasznalo)
        .filter(
            model_felhasznalo.Felhasznalo.felhasznalonev == felhasznalo.felhasznalonev
        )
        .first()
    )

    if db_felhasznalo is None:
        raise HTTPException(status_code=404, detail="Nincs ilyen felhasznalo")

    if not sha256_crypt.verify(felhasznalo.jelszo, db_felhasznalo.jelszo):
        raise HTTPException(status_code=404, detail="Hibas jelszo")

    return db_felhasznalo


def felhasznalo_by_felhasznalonev(felhasznalonev: str, db: Session):
    db_felhasznalo = (
        db.query(model_felhasznalo.Felhasznalo)
        .filter(model_felhasznalo.Felhasznalo.felhasznalonev == felhasznalonev)
        .first()
    )

    if db_felhasznalo is None:
        raise HTTPException(status_code=404, detail="Nincs ilyen felhasznalo")

    return db_felhasznalo
