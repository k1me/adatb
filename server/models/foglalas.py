from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from database import Base
from models.vendeg import Vendeg


class Foglalas(Base):
    __tablename__ = "foglalas"

    email = Column(String, ForeignKey(Vendeg.email), primary_key=True, index=True)
    mettol = Column(DateTime, primary_key=True, index=True)
    meddig = Column(DateTime, primary_key=True, index=True)
    fizetendo = Column(Integer)
