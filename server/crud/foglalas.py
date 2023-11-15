from sqlalchemy.orm import Session
from models import foglalas as model_foglalas
from schemas import foglalas as schema_foglalas


def foglalas_create(foglalas: schema_foglalas.FoglalasCreate, db: Session):
    db_foglalas = model_foglalas.Foglalas(email=foglalas.email, mettol=foglalas.mettol, meddig=foglalas.meddig, fizetendo=foglalas.fizetendo)
    db.add(db_foglalas)
    db.commit()
    db.refresh(db_foglalas)
    return db_foglalas

def foglalas_list(db: Session):
    return db.query(model_foglalas.Foglalas).all()