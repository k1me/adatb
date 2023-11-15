from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from database import Base


class SzobaTipus(Base):
    __tablename__ = "szobatipus"
    
    megnevezes = Column(String, primary_key=True, index=True)
    napi_ar = Column(Integer)
    fekvohelyek_szama = Column(Integer)
    leiras = Column(Text)


class Szoba(Base):
    __tablename__ = "szoba"
    
    szobaszam = Column(Integer, primary_key=True, index=True)
    megnevezes = Column(String, ForeignKey("szobatipus.megnevezes"), primary_key=True, index=True)

class Vendeg(Base):
    __tablename__ = "vendeg"
    
    email = Column(String, primary_key=True, index=True)
    nev = Column(String)
    telefonszam = Column(String)
    szuletesi_datum = Column(DateTime)

class Felhasznalo(Base):
    __tablename__ = "felhasznalo"
    
    felhasznalonev = Column(String, primary_key=True, index=True)
    nev = Column(String)
    jelszo = Column(String)

class Foglalas(Base):
    __tablename__ = "foglalas"
    
    email = Column(String, ForeignKey("vendeg.email"), primary_key=True, index=True)
    mettol = Column(DateTime, primary_key=True, index=True)
    meddig = Column(DateTime, primary_key=True, index=True)
    fizetendo = Column(Integer)
    
class Kezeli(Base):
    __tablename__ = "kezeli"
    
    felhasznalonev = Column(String, ForeignKey("felhasznalo.felhasznalonev"), primary_key=True, index=True)
    email = Column(String, ForeignKey("vendeg.email"), primary_key=True, index=True)
    mettol = Column(DateTime, primary_key=True, index=True)
    meddig = Column(DateTime, primary_key=True, index=True)
    
class Szobaja(Base):
    __tablename__ = "szobaja"
    
    email = Column(String, ForeignKey("vendeg.email"), primary_key=True, index=True)
    szobaszam = Column(Integer, ForeignKey("szoba.szobaszam"), primary_key=True, index=True)
    mettol = Column(DateTime, primary_key=True, index=True)
    meddig = Column(DateTime, primary_key=True, index=True)