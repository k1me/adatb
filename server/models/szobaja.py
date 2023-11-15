from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from database import Base
from models.szoba import Szoba
from models.vendeg import Vendeg
from models.foglalas import Foglalas
    
class Szobaja(Base):
    __tablename__ = "szobaja"
    
    email = Column(String, ForeignKey(Vendeg.email), primary_key=True, index=True)
    szobaszam = Column(Integer, ForeignKey(Szoba.szobaszam), primary_key=True, index=True)
    mettol = Column(DateTime, ForeignKey(Foglalas.mettol), primary_key=True, index=True)
    meddig = Column(DateTime, ForeignKey(Foglalas.meddig), primary_key=True, index=True)