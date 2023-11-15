from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine

from models import szoba as model_szoba

from schemas import (
    szobatipus as schema_szobatipus,
    szoba as schema_szoba,
    vendeg as schema_vendeg,
    felhasznalo as schema_felhasznalo,
    foglalas as schema_foglalas,
    kezeli as schema_kezeli,
    szobaja as schema_szobaja
)

from crud import (
    szobatipus as crud_szobatipus,
    szoba as crud_szoba,
    vendeg as crud_vendeg,
    felhasznalo as crud_felhasznalo,
    foglalas as crud_foglalas,
    kezeli as crud_kezeli,
    szobaja as crud_szobaja
)

model_szoba.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SzobaTipus-----------------------------------------------------------------------------------

@app.post("/szobatipus")
def szobatipus_create(szobatipus: schema_szobatipus.SzobaTipusCreate, db: Session = Depends(get_db)):
    
    return crud_szobatipus.szobatipus_create(szobatipus, db)

@app.get("/szobatipus")
def szobatipus_list(db: Session = Depends(get_db)):
    return crud_szobatipus.szobatipus_list(db)

@app.get("/szobatipus/{megnevezes}")
def szobatipus_by_megnevezes(megnevezes: str, db: Session = Depends(get_db)):
    return crud_szobatipus.szobatipus_by_megnevezes(megnevezes, db)

# Szoba---------------------------------------------------------------------------------------

@app.post("/szoba")
def szoba_create(szoba: schema_szoba.SzobaCreate, db: Session = Depends(get_db)):
    return crud_szoba.szoba_create(szoba, db)

@app.get("/szoba")
def szoba_list(db: Session = Depends(get_db)):
    return crud_szoba.szoba_list(db)

@app.get("/szoba/szobaszam/{szobaszam}")
def szoba_by_szobaszam(szobaszam: int, db: Session = Depends(get_db)):
    return crud_szoba.szoba_by_szobaszam(szobaszam, db)

@app.get("/szoba/megnevezes/{megnevezes}")
def szoba_by_megnevezes(megnevezes: str, db: Session = Depends(get_db)):
    return crud_szoba.szoba_by_megnevezes(megnevezes, db)

# Vendeg--------------------------------------------------------------------------------------

@app.post("/vendeg")
def vendeg_create(vendeg: schema_vendeg.VendegCreate, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_create(vendeg, db)

@app.get("/vendeg")
def vendeg_list(db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_list(db)

@app.get("/vendeg/email/{email}")
def vendeg_by_email(email: str, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_by_email(email, db)

@app.get("/vendeg/nev/{nev}")
def vendeg_by_nev(nev: str, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_by_nev(nev, db)

@app.get("/vendeg/datum/{datum}")
def vendeg_by_datum(datum: str, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_by_datum(datum, db)

@app.get("/vendeg/fiatalabb/{ev}")
def vendeg_fiatalabb(ev: int, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_fiatalabb(ev, db)

@app.get("/vendeg/idosebb/{ev}")
def vendeg_idosebb(ev: int, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_idosebb(ev, db)

# Felhasznalo--------------------------------------------------------------------------------------

@app.post("/felhasznalo")
def felhasznalo_create(felhasznalo: schema_felhasznalo.FelhasznaloCreate, db: Session = Depends(get_db)):
    return crud_felhasznalo.felhasznalo_create(felhasznalo, db)

@app.post("/felhasznalo/login")
def felhasznalo_login(felhasznalonev: str, jelszo: str, db: Session = Depends(get_db)):
    return crud_felhasznalo.felhasznalo_login(felhasznalonev, jelszo, db)

# Foglalas--------------------------------------------------------------------------------------

@app.post("/foglalas")
def foglalas_create(foglalas: schema_foglalas.FoglalasCreate, db: Session = Depends(get_db)):
    return crud_foglalas.foglalas_create(foglalas, db)

@app.get("/foglalas")
def foglalas_list(db: Session = Depends(get_db)):
    return crud_foglalas.foglalas_list(db)

# Kezeli---------------------------------------------------------------------------------------

@app.post("/kezeli")
def kezeli_create(kezeli: schema_kezeli.KezeliCreate, db: Session = Depends(get_db)):
    return crud_kezeli.kezeli_create(kezeli, db)

@app.get("/kezeli")
def kezeli_list(db: Session = Depends(get_db)):
    return crud_kezeli.kezeli_list(db)

@app.get("/kezeli/felhasznalonev/{felhasznalonev}")
def kezeli_by_felhasznalonev(felhasznalonev: str, db: Session = Depends(get_db)):
    return crud_kezeli.kezeli_by_felhasznalonev(felhasznalonev, db)

# Szobaja---------------------------------------------------------------------------------------

@app.post("/szobaja")
def szobaja_create(szobaja: schema_szobaja.SzobajaCreate, db: Session = Depends(get_db)):
    return crud_szobaja.szobaja_create(szobaja, db)

@app.get("/szobaja")
def szobaja_list(db: Session = Depends(get_db)):
    return crud_szobaja.szobaja_list(db)