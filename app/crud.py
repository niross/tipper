import os
import shutil

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app import config, models, schemas


def get_tip_report(db: Session, tip_report_id: int):
    return (
        db.query(models.TipReport).filter(models.TipReport.id == tip_report_id).first()
    )


def create_tip_report(db: Session, tip_report: schemas.TipReport):
    db_tip_report = models.TipReport(**tip_report.dict())
    db.add(db_tip_report)
    db.commit()
    db.refresh(db_tip_report)
    return db_tip_report


def attach_image(db: Session, tip_report: schemas.TipReport, image: UploadFile):
    file_loc = os.path.join(
        config.ATTACHMENTS_DIR, f"{str(tip_report.id)}-{image.filename}"
    )
    with open(file_loc, "wb+") as fh:
        shutil.copyfileobj(image.file, fh)
    tip_report.image = file_loc
    db.commit()
