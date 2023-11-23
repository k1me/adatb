from sqlalchemy import Column, String
from database import Base


class Felhasznalo(Base):
    __tablename__ = "felhasznalo"

    felhasznalonev = Column(String, primary_key=True, index=True)
    nev = Column(String)
    jelszo = Column(String)
