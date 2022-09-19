from sqlalchemy.orm import Session

from app import models, schemas


def create_tip_report(db: Session, tip_report: schemas.TipReport):
    db_tip_report = models.TipReport(**tip_report.dict())
    db.add(db_tip_report)
    db.commit()
    db.refresh(db_tip_report)
    return db_tip_report
