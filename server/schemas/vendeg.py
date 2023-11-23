from datetime import date
from pydantic import BaseModel


class VendegCreate(BaseModel):
    email: str
    nev: str
    telefonszam: str
    szuletesi_datum: date
