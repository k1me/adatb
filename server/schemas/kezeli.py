from pydantic import BaseModel

from schemas import felhasznalo, vendeg


class KezeliBase(BaseModel):
    felhasznalonev: str
    email: str

class KezeliCreate(KezeliBase):
    pass

class Kezeli(KezeliBase):
    felhasznalo: felhasznalo.Felhasznalo
    vendeg: vendeg.Vendeg

    class Config:
        orm_mode = True
