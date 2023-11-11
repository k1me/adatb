import datetime
from pydantic import BaseModel

from schemas import szoba, foglalas, vendeg


class SzobajaBase(BaseModel):
    szobaszam: int
    mettol: datetime
    meddig: datetime
    email: str

class SzobajaCreate(SzobajaBase):
    pass

class Szobaja(SzobajaBase):
    szoba: szoba.Szoba
    foglalas: foglalas.Foglalas
    vendeg: vendeg.Vendeg

    class Config:
        orm_mode = True
