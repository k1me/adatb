import datetime
from typing import List
from pydantic import BaseModel

from schemas import felhasznalo, vendeg, szoba


class FoglalasBase(BaseModel):
    email: str
    mettol: datetime
    meddig: datetime
    fizetendo: int

class FoglalasCreate(FoglalasBase):
    pass

class Foglalas(FoglalasBase):
    felhasznalo: felhasznalo.Felhasznalo
    vendeg: vendeg.Vendeg
    szoba: szoba.Szoba

    class Config:
        orm_mode = True
