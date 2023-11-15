from sqlalchemy import Column, DateTime, String
from database import Base

class Vendeg(Base):
    __tablename__ = "vendeg"
    
    email = Column(String, primary_key=True, index=True)
    nev = Column(String)
    telefonszam = Column(String)
    szuletesi_datum = Column(DateTime)