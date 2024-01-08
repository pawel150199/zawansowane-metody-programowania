from typing import Any, Dict, Union

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from src.models.report import Report as Report
from src.models.user import User
from src.schemas.report import CreateReport, UpdateReport


# POST
def create_report(db: Session, report: CreateReport, user_id: int):
    db_report = Report(
        title=report.title, status=report.status, user_id=user_id
    )

    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report


# GET
def get_report(db: Session, report_id: int):
    return (
        db.query(Report)
        .filter(Report.id == report_id)
        .first()
    )


def get_report_by_user(db: Session, user_id: int):
    return db.query(Report).filter(Report.user_id == user_id).all()


def get_report_by_group(db: Session, group_id: int):
    return db.query(Report).join(User).filter(User.group_id == group_id).all()


# DELETE
def delete_report(db: Session, report_id: int):
    db_report = db.query(Report).get(report_id)
    db.delete(db_report)
    db.commit()
    return db_report


# UPDATE
def update_report(
    db: Session,
    report_obj: Report,
    report_in: Union[UpdateReport, Dict[str, Any]],
) -> Report:
    obj_data = jsonable_encoder(report_obj)
    if isinstance(report_in, dict):
        update_data = report_in
    else:
        update_data = report_in.dict(exclude_unset=True)

    for field in obj_data:
        if field in update_data:
            setattr(report_obj, field, update_data[field])
    db.add(report_obj)
    db.commit()
    db.refresh(report_obj)
    return report_obj
