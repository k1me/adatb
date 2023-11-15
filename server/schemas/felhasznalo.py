from pydantic import BaseModel

class FelhasznaloCreate(BaseModel):
    felhasznalonev: str
    nev: str
    jelszo: str
    
    class Config:
        orm_mode = True
        
class Felhasznalo(BaseModel):
    felhasznalonev: str
    nev: str
    
    class Config:
        orm_mode = True