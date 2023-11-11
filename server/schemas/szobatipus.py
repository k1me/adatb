from typing import List
from pydantic import BaseModel

from schemas import szoba

class SzobatipusBase(BaseModel):
    megnevezes: str
    napi_ar: int
    fekvohelyek_szama: int
    leiras: str

class SzobatipusCreate(SzobatipusBase):
    pass

class Szobatipus(SzobatipusBase):
    szobak: List["szoba.Szoba"] = []

    class Config:
        orm_mode = True

