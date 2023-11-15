from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base
from models.szobatipus import SzobaTipus


class Szoba(Base):
    __tablename__ = "szoba"
    
    szobaszam = Column(Integer, primary_key=True, index=True)
    megnevezes = Column(String, ForeignKey(SzobaTipus.megnevezes), primary_key=True, index=True)
