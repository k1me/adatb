from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud

from models import models
from schemas import FelhasznaloCreate, felhasznalo
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/felhasznalok/", response_model=felhasznalo)
def create_user(user: FelhasznaloCreate, db: Session = Depends(get_db)):
    db_user = felhasznalo(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
