from pydantic import BaseModel


class FelhasznaloCreate(BaseModel):
    felhasznalonev: str
    nev: str
    jelszo: str

    class Config:
        from_attributes = True


class Bejelentkezes(BaseModel):
    felhasznalonev: str
    jelszo: str

    class Config:
        from_attributes = True


class Felhasznalo(BaseModel):
    felhasznalonev: str
    nev: str

    class Config:
        from_attributes = True
