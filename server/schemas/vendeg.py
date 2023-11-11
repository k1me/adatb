import datetime
from typing import List
from pydantic import BaseModel

from schemas import foglalas


class VendegBase(BaseModel):
    email: str
    nev: str
    telefon: str
    szuletesi_datum: datetime

class VendegCreate(VendegBase):
    pass

class Vendeg(VendegBase):
    foglalasok: List["foglalas.Foglalas"] = []

    class Config:
        orm_mode = True

