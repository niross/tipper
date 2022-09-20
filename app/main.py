from typing import Union

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/reports/", response_model=schemas.TipReport)
def create_tip_report(tip_report: schemas.TipReport, db: Session = Depends(get_db)):
    return crud.create_tip_report(db=db, tip_report=tip_report)
