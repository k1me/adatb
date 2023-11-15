from datetime import date
from pydantic import BaseModel

class SzobajaCreate(BaseModel):
    email: str
    mettol: date
    meddig: date
    szobaszam: int