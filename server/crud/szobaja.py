from sqlalchemy.orm import Session
from models import szobaja as model_szobaja 
from schemas import szobaja as schema_szobaja


def szobaja_create(altSzobaja: schema_szobaja.SzobajaRnRt, db: Session):
    for szoba in altSzobaja.selectedRooms:
        db_szobaja = model_szobaja.Szobaja(email=altSzobaja.email, szobaszam=szoba.szobaszam, mettol=altSzobaja.mettol, meddig=altSzobaja.meddig)
        db.add(db_szobaja)
    db.commit()
    db.refresh(db_szobaja)
    return db_szobaja

def szobaja_list(db: Session):
    return db.query(model_szobaja.Szobaja).all()