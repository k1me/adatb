from sqlalchemy.orm import Session
from models import szobaja as model_szobaja 
from schemas import szobaja as schema_szobaja


def szobaja_create(szobaja: schema_szobaja.SzobajaCreate, db: Session):
    db_szobaja = model_szobaja.Szobaja(email=szobaja.email, szobaszam=szobaja.szobaszam, mettol=szobaja.mettol, meddig=szobaja.meddig)
    db.add(db_szobaja)
    db.commit()
    db.refresh(db_szobaja)
    return db_szobaja

def szobaja_list(db: Session):
    return db.query(model_szobaja.Szobaja).all()