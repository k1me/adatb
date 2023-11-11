from pydantic import BaseModel

from schemas import felhasznalo, vendeg, foglalas


class SzobaBase(BaseModel):
    szobaszam: int
    megnevezes: str

class SzobaCreate(SzobaBase):
    pass

class Szoba(SzobaBase):
    felhasznalo: felhasznalo.Felhasznalo
    vendeg: vendeg.Vendeg
    foglalas: foglalas.Foglalas

    class Config:
        orm_mode = True
