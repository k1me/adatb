from pydantic import BaseModel

class SzobaCreate(BaseModel):
    szobaszam: int
    megnevezes: str
