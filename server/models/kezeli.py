from sqlalchemy import Column, ForeignKey, String, DateTime
from database import Base
from models.felhasznalo import Felhasznalo
from models.vendeg import Vendeg


class Kezeli(Base):
    __tablename__ = "kezeli"

    felhasznalonev = Column(
        String, ForeignKey(Felhasznalo.felhasznalonev), primary_key=True, index=True
    )
    email = Column(String, ForeignKey(Vendeg.email), primary_key=True, index=True)
    mettol = Column(DateTime, primary_key=True, index=True)
    meddig = Column(DateTime, primary_key=True, index=True)
