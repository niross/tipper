#!/usr/bin/env python
import argparse
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import config, crud

engine = create_engine(config.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()


def main():
    parser = argparse.ArgumentParser(prog="Send tip report")
    parser.add_argument("report_id", type=int)
    args = parser.parse_args()
    report = crud.get_tip_report(db, args.report_id)
    if report is None:
        print(f"No tip report found with id {args.report_id}")
        return
    if report.sent is not None:
        print("This report has already been sent")

    # TODO: Send the tip report

    # report.sent = datetime.utcnow()
    # db.commit()


if __name__ == "__main__":
    main()
