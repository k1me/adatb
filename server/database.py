from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#itt a port szám nem biztos hogy minden gépen 3306 lesz
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost:3306/szalloda"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
