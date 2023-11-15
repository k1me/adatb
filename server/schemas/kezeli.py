from datetime import date
from pydantic import BaseModel

class KezeliCreate(BaseModel):
    felhasznalonev: str
    email: str
    mettol: date
    meddig: date
    