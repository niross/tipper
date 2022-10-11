from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


api_app = FastAPI(title="API")
app = FastAPI(title="Main App")
app.mount("/api", api_app)
app.mount("/", StaticFiles(directory="app/frontend", html=True), name="frontend")


@api_app.post("/reports/", response_model=schemas.TipReport)
async def create_tip_report(
    tip_report: schemas.TipReport, db: Session = Depends(get_db)
):
    return crud.create_tip_report(db=db, tip_report=tip_report)
