from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Felhasznalo(Base):
    __tablename__ = "felhasznalo"
    
    felhasznalonev = Column(String, primary_key=True, index=True)
    nev = Column(String)
    hashed_jelszo = Column(String)
    
    foglalasok = relationship("Foglalas", back_populates="felhasznalo", lazy="dynamic")
    szobak = relationship("Szoba", back_populates="felhasznalo", lazy="dynamic")
        

class Vendeg(Base):
    __tablename__ = "vendeg"
    
    email = Column(String, primary_key=True, index=True)
    nev = Column(String)
    telefon = Column(String(20))
    szuletesi_datum = Column(DateTime)
    
    foglalasok = relationship("Foglalas", back_populates="vendeg", lazy="dynamic")
    
    
class Szobatipus(Base):
    __tablename__ = "szobatipus"
    
    megnevezes = Column(String, primary_key=True, index=True)
    napi_ar = Column(Integer)
    fekvohelyek_szama = Column(Integer)
    leiras = Column(String)
    
    szobak = relationship("Szoba", back_populates="szobatipus", lazy="dynamic")
    
    
class Foglalas(Base):
    __tablename__ = "foglalas"
    email = Column(String, ForeignKey("vendeg.email"), primary_key=True, index=True)
    mettol = Column(DateTime, primary_key=True, index=True)
    meddig = Column(DateTime, primary_key=True, index=True)
    fizetendő = Column(Integer)
    
    felhasznalo = relationship("Felhasznalo", back_populates="foglalasok", lazy="dynamic")
    vendeg = relationship("Vendeg", back_populates="foglalasok", lazy="dynamic")
    szoba = relationship("Szoba", back_populates="foglalasok", lazy="dynamic")
    

class Szoba(Base):
    __tablename__ = "szoba"
    szobaszam = Column(Integer, primary_key=True, index=True)
    megnevezes = Column(String, ForeignKey("szobatipus.megnevezes"), primary_key=True, index=True)
    
    felhasznalo = relationship("Felhasznalo", back_populates="szobak", lazy="dynamic")
    vendeg = relationship("Vendeg", back_populates="szobak", lazy="dynamic")
    foglalas = relationship("Foglalas", back_populates="szobak", lazy="dynamic")    
    
    
class Kezeli(Base):
    __tablename__ = "kezeli"
    felhasznalonev = Column(String, ForeignKey("felhasznalo.felhasznalonev"), primary_key=True, index=True)
    email = Column(String, ForeignKey("vendeg.email"), primary_key=True, index=True)
    
    felhasznalo = relationship("Felhasznalo", back_populates="kezeli", lazy="dynamic")
    vendeg = relationship("Vendeg", back_populates="kezeli", lazy="dynamic")
    
class Szobaja(Base):
    __tablename__ = "szobaja"
    szobaszam = Column(Integer, ForeignKey("szoba.szobaszam"), primary_key=True, index=True)
    mettol = Column(DateTime, ForeignKey("foglalas.mettol"), primarykey=True, index=True)
    meddig = Column(DateTime, ForeignKey("foglalas.meddig"), primarykey=True, index=True)
    email = Column(String, ForeignKey("vendeg.email"), primary_key=True, index=True)
    
    szoba = relationship("Szoba", back_populates="szobaja", lazy="dynamic")
    foglalas = relationship("Foglalas", back_populates="szobaja", lazy="dynamic")
    vendeg = relationship("Vendeg", back_populates="szobaja", lazy="dynamic")