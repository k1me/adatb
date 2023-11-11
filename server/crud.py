from sqlalchemy.orm import Session

from models import Felhasznalo
from schemas import Crea, FelhasznaloCreate


def get_felhasznalo(db:Session, felhasznalonev: str):
    return db.query(Felhasznalo).filter(Felhasznalo.felhasznalonev == felhasznalonev).first()


def create_felhasznalo(db: Session, vendeg: FelhasznaloCreate):
    db_felhasznalo = Felhasznalo(
        felhasznalonev=vendeg.felhasznalonev, 
        nev=vendeg.nev, 
        hashed_jelszo=vendeg.hashed_jelszo
    )
    db.add(db_felhasznalo)
    db.commit()
    db.refresh(db_felhasznalo)
    return db_felhasznalo
