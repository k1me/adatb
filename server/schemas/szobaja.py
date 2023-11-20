from datetime import date
from pydantic import BaseModel

class SzobajaCreate(BaseModel):
    email: str
    mettol: date
    meddig: date
    szobaszam: int
    
    
#SzobajaRoomNumberAndRoomType roviden SzobajaRnRt
#csak a szobaszamot es a szobatipust tartalmazza
class SzobajaRnRt(BaseModel):
    megnevezes: str
    szobaszam: int
    
class SzobajaAltered(BaseModel):
    email: str
    mettol: date
    meddig: date
    selectedRooms: list[SzobajaRnRt]