from datetime import date
from pydantic import BaseModel


class FoglalasCreate(BaseModel):
    email: str
    mettol: date
    meddig: date
    fizetendo: int
