import io

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.main import app, get_db
from app.models import TipReport

SQLALCHEMY_DATABASE_URL = "sqlite:///app/test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)


# TODO: Will need to be upgraded to async tests in the future
def test_create_report(test_db):
    session = TestingSessionLocal()
    tip_report_count = session.query(TipReport).count()
    response = client.post(
        "/api/reports/",
        json={
            "latitude": 1.1,
            "longitude": -1.1,
            "number_of_items": 2,
            "description": "A test report",
            "is_hazardous": False,
            "reporter_title": "Sir",
            "reporter_first_name": "Bob",
            "reporter_last_name": "Testeroni",
            "reporter_email": "bob.testeroni@gmail.com",
            "reporter_phone": "+15554545",
        },
    )
    assert response.status_code == 200
    assert session.query(TipReport).count() == tip_report_count + 1


# TODO: Attach image tests
def test_attach_image(test_db):
    image = io.BytesIO(b"")

    # Tip report doesn't exist
    response = client.post("/api/reports/99/attach/", files={"image": image})
    assert response.status_code == 404

    # Tip report exists
    report = client.post(
        "/api/reports/",
        json={
            "latitude": 1.1,
            "longitude": -1.1,
        },
    ).json()
    response = client.post(
        f"/api/reports/{report['id']}/attach/", files={"image": image}
    )
    assert response.status_code == 200
    session = TestingSessionLocal()
    assert (
        session.query(TipReport).order_by(TipReport.id.desc()).first().image is not None
    )
