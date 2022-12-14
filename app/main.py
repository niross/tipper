import sentry_sdk
from fastapi import Depends, FastAPI, HTTPException, UploadFile
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app import config, crud, models, schemas
from app.database import engine
from app.notify import send_slack_message
from app.utils import get_db


sentry_sdk.init(
    dsn=config.SENTRY_DSN,
    traces_sample_rate=1.0,
)

models.Base.metadata.create_all(bind=engine)

api_app = FastAPI(title="API")
app = FastAPI(title="Main App")
app.mount("/api", api_app)
app.mount("/", StaticFiles(directory="app/frontend", html=True), name="frontend")


@api_app.post("/reports/", response_model=schemas.TipReport)
async def create_tip_report(
    tip_report: schemas.TipReport, db: Session = Depends(get_db)
):
    report = crud.create_tip_report(db=db, tip_report=tip_report)
    send_slack_message(f"Tip report with id {report.id} created")
    return report


@api_app.post("/reports/{tip_report_id}/attach/")
async def attach_image(
    tip_report_id: int, image: UploadFile, db: Session = Depends(get_db)
):
    tip_report = crud.get_tip_report(db=db, tip_report_id=tip_report_id)
    if tip_report is None:
        raise HTTPException(status_code=404, detail="Tip report not found")
    crud.attach_image(db=db, tip_report=tip_report, image=image)
    return {"tip_report_id": tip_report_id, "filename": image.filename}
