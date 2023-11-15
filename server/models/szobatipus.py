from sqlalchemy import Column,  Integer, String, Text
from database import Base

class SzobaTipus(Base):
    __tablename__ = "szobatipus"
    
    megnevezes = Column(String, primary_key=True, index=True)
    napi_ar = Column(Integer)
    fekvohelyek_szama = Column(Integer)
    leiras = Column(Text)