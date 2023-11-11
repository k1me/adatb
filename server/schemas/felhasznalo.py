from typing import List
from pydantic import BaseModel

from schemas import foglalas, szoba


class FelhasznaloBase(BaseModel):
    felhasznalonev: str
    nev: str

class FelhasznaloCreate(FelhasznaloBase):
    hashed_jelszo: str

class Felhasznalo(FelhasznaloBase):
    foglalasok: List["foglalas.Foglalas"] = []
    szobak: List["szoba.Szoba"] = []

    class Config:
        orm_mode = True
