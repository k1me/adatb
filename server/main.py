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

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SzobaTipus-----------------------------------------------------------------------------------

@app.post("/szobatipus", tags=["Szobatipus", "Create"])
def szobatipus_create(szobatipus: schema_szobatipus.SzobaTipusCreate, db: Session = Depends(get_db)):
    return crud_szobatipus.szobatipus_create(szobatipus, db)

@app.get("/szobatipusok", tags=["Szobatipus", "Read"])
def szobatipus_list(db: Session = Depends(get_db)):
    return crud_szobatipus.szobatipus_list(db)

@app.put("/szobatipus/{megnevezes}", tags=["Szobatipus", "Update"])
def szobatipus_update(szobatipus: schema_szobatipus.SzobaTipusCreate, db: Session = Depends(get_db)):
    return crud_szobatipus.szobatipus_update(szobatipus, db)

@app.delete("/szobatipus/{megnevezes}", tags=["Szobatipus", "Delete"])
def szobatipus_delete(megnevezes: str, db: Session = Depends(get_db)):
    return crud_szobatipus.szobatipus_delete(megnevezes, db)

@app.get("/szobatipus/{megnevezes}", tags=["Szobatipus", "Read"])
def szobatipus_by_megnevezes(megnevezes: str, db: Session = Depends(get_db)):
    return crud_szobatipus.szobatipus_by_megnevezes(megnevezes, db)

# Szoba---------------------------------------------------------------------------------------

@app.post("/szoba", tags=["Szoba", "Create"])
def szoba_create(szoba: schema_szoba.SzobaCreate, db: Session = Depends(get_db)):
    return crud_szoba.szoba_create(szoba, db)

@app.get("/szobak", tags=["Szoba", "Read"])
def szoba_list(db: Session = Depends(get_db)):
    return crud_szoba.szoba_list(db)

@app.put("/szoba/{szobaszam}", tags=["Szoba", "Update"])
def szoba_update(szobaszam: int, szoba: schema_szoba.SzobaCreate, db: Session = Depends(get_db)):
    return crud_szoba.szoba_update(szobaszam, szoba, db)

@app.delete("/szoba/{szobaszam}", tags=["Szoba", "Delete"])
def szoba_delete(szobaszam: int, db: Session = Depends(get_db)):
    return crud_szoba.szoba_delete(szobaszam, db)

@app.get("/szoba/szobaszam/{szobaszam}", tags=["Szoba", "Read"])
def szoba_by_szobaszam(szobaszam: int, db: Session = Depends(get_db)):
    return crud_szoba.szoba_by_szobaszam(szobaszam, db)

@app.get("/szoba/megnevezes/{megnevezes}", tags=["Szoba", "Read"])
def szoba_by_megnevezes(megnevezes: str, db: Session = Depends(get_db)):
    return crud_szoba.szoba_by_megnevezes(megnevezes, db)

# Vendeg--------------------------------------------------------------------------------------

@app.post("/vendeg", tags=["Vendég", "Create"])
def vendeg_create(vendeg: schema_vendeg.VendegCreate, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_create(vendeg, db)

@app.get("/vendegek", tags=["Vendég", "Read"])
def vendeg_list(db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_list(db)

@app.put("/vendeg/{email}", tags=["Vendég", "Update"])
def vendeg_update(email: str, vendeg: schema_vendeg.VendegCreate, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_update(email, vendeg, db)

@app.delete("/vendeg/{email}", tags=["Vendég", "Delete"])
def vendeg_delete(email: str, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_delete(email, db)

@app.get("/vendeg/email/{email}", tags=["Vendég", "Read"])
def vendeg_by_email(email: str, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_by_email(email, db)

@app.get("/vendeg/nev/{nev}", tags=["Vendég", "Read"])
def vendeg_by_nev(nev: str, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_by_nev(nev, db)

@app.get("/vendeg/datum/{datum}", tags=["Vendég", "Read"])
def vendeg_by_datum(datum: str, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_by_datum(datum, db)

@app.get("/vendeg/fiatalabb/{ev}", tags=["Vendég", "Read"])
def vendeg_fiatalabb(ev: int, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_fiatalabb(ev, db)

@app.get("/vendeg/idosebb/{ev}", tags=["Vendég", "Read"])
def vendeg_idosebb(ev: int, db: Session = Depends(get_db)):
    return crud_vendeg.vendeg_idosebb(ev, db)

# Felhasznalo--------------------------------------------------------------------------------------

@app.post("/felhasznalo/register", tags=["Felhasználó", "Create"])
def felhasznalo_create(felhasznalo: schema_felhasznalo.FelhasznaloCreate, db: Session = Depends(get_db)):
    return crud_felhasznalo.felhasznalo_create(felhasznalo, db)

@app.get("/felhasznalok", tags=["Felhasználó", "Read"])
def felhasznalo_list(db: Session = Depends(get_db)):
    return crud_felhasznalo.felhasznalo_list(db)

@app.put("/felhasznalo/{felhasznalonev}", tags=["Felhasználó", "Update"])
def felhasznalo_update(felhasznalonev: str, felhasznalo: schema_felhasznalo.FelhasznaloCreate, db: Session = Depends(get_db)):
    return crud_felhasznalo.felhasznalo_update(felhasznalonev, felhasznalo, db)

@app.delete("/felhasznalo/{felhasznalonev}", tags=["Felhasználó", "Delete"])
def felhasznalo_delete(felhasznalonev: str, db: Session = Depends(get_db)):
    return crud_felhasznalo.felhasznalo_delete(felhasznalonev, db)

@app.post("/felhasznalo/login", tags=["Felhasználó", "Create"])
def felhasznalo_login(felhasznalo: schema_felhasznalo.Bejelentkezes, db: Session = Depends(get_db)):
    return crud_felhasznalo.felhasznalo_login(felhasznalo, db)

@app.get('/felhasznalo/{felhasznalonev}', tags=["Felhasználó", "Read"])
def felhasznalo_by_felhasznalonev(felhasznalonev: str, db: Session = Depends(get_db)):
    return crud_felhasznalo.felhasznalo_by_felhasznalonev(felhasznalonev, db)



# Foglalas--------------------------------------------------------------------------------------

@app.post("/foglalas", tags=["Foglalás", "Create"])
def foglalas_create(foglalas: schema_foglalas.FoglalasCreate, db: Session = Depends(get_db)):
    return crud_foglalas.foglalas_create(foglalas, db)

@app.get("/foglalasok", tags=["Foglalás", "Read"])
def foglalas_list(db: Session = Depends(get_db)):
    return crud_foglalas.foglalas_list(db)

@app.put("/foglalas/{email}", tags=["Foglalás", "Update"])
def foglalas_update(email: str, foglalas: schema_foglalas.FoglalasCreate, db: Session = Depends(get_db)):
    return crud_foglalas.foglalas_update(email, foglalas, db)

@app.delete("/foglalas/{email}", tags=["Foglalás", "Delete"])
def foglalas_delete(email: str, db: Session = Depends(get_db)):
    return crud_foglalas.foglalas_delete(email, db)

# Kezeli---------------------------------------------------------------------------------------

@app.post("/kezeli", tags=["Kezeli", "Create"])
def kezeli_create(kezeli: schema_kezeli.KezeliCreate, db: Session = Depends(get_db)):
    return crud_kezeli.kezeli_create(kezeli, db)

@app.get("/kezeli", tags=["Kezeli", "Read"])
def kezeli_list(db: Session = Depends(get_db)):
    return crud_kezeli.kezeli_list(db)

@app.get("/kezeli/felhasznalonev/{felhasznalonev}", tags=["Kezeli", "Read"])
def kezeli_by_felhasznalonev(felhasznalonev: str, db: Session = Depends(get_db)):
    return crud_kezeli.kezeli_by_felhasznalonev(felhasznalonev, db)

# Szobaja---------------------------------------------------------------------------------------

@app.post("/szobaja", tags=["Szobája", "Create"])
def szobaja_create(szobaja: schema_szobaja.SzobajaCreate, db: Session = Depends(get_db)):
    return crud_szobaja.szobaja_create(szobaja, db)

@app.get("/szobaja", tags=["Szobája", "Read"])
def szobaja_list(db: Session = Depends(get_db)):
    return crud_szobaja.szobaja_list(db)