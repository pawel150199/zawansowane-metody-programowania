from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src import crud, models, schemas
from src.api.helper import (get_current_teamadmin, get_current_user,
                            get_current_webadmin,
                            get_current_webadmin_or_teamadmin, get_db)

router = APIRouter()

# POST
@router.post("/me/reports/", response_model=schemas.Report)
def create_report(
    report: schemas.CreateMyReport,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
) -> Any:
    report_in = crud.get_report_by_user(db, user_id=current_user.id)
    if any(
        report.title == report.title and report.status == report.status
        for report in report_in
    ):
        raise HTTPException(status_code=400, detail="Similar report exist")
    return crud.create_report(
        db=db, report=report, user_id=current_user.id
    )


# GET
@router.get("/group/reports/", response_model=list[schemas.Report])
def read_reports_in_my_group(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_teamadmin),
) -> Any:
    reports = crud.get_report_by_group(db, group_id=current_user.group_id)
    if reports is None or reports == []:
        raise HTTPException(status_code=404, detail="Reports not found")
    return reports


# @router.get("/reports/", response_model=list[schemas.Report])
# def read_reports(db: Session = Depends(get_db)):
#    reports = crud.get_reports(db)
#    if reports == [] or reports is None:
#        raise HTTPException(
#            status_code=404,
#            detail="Reports not found"
#        )
#    return reports

@router.get("/reports/{report_id}", response_model=schemas.Report)
def read_report(report_id: int, db: Session = Depends(get_db), _: models.User = Depends(get_current_teamadmin)):
    db_report = crud.get_report(db=db, report_id=report_id)
    if db_report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )
    return db_report


@router.get("/me/reports", response_model=list[schemas.Report])
def read_report_by_user(
    db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)
) -> Any:
    me = current_user.id
    db_report = crud.get_report_by_user(db=db, user_id=me)
    if db_report is None or db_report == []:
        raise HTTPException(status_code=404, detail="Reports not found")
    return db_report


# @router.get("/reports/user/{user_id}", response_model=list[schemas.Report])
# def read_report_by_user(user_id: int, db: Session = Depends(get_db)):
#    db_report = crud.get_report_by_user(db=db, user_id=user_id)
#    if db_report is None:
#        raise HTTPException(
#            status_code=404,
#            detail="Report not found"
#        )
#    return db_report

# DELETE
@router.delete(
    "/report/delete/{report_id}", response_model=schemas.Report
)
def delete_report(
    report_id: int,
    db: Session = Depends(get_db),
    _: models.User = Depends(get_current_webadmin),
) -> Any:
    report = crud.get_report(db=db, report_id=report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Raport not found")
    report = crud.delete_report(db=db, report_id=report_id)
    return report


# UPDATE
@router.put("/report/{report_id}", response_model=schemas.Report)
def update_report(
    report_id: int,
    report_in: schemas.UpdateReport,
    db: Session = Depends(get_db),
    _: models.Report = Depends(get_current_webadmin_or_teamadmin),
) -> Any:
    report = crud.get_report(db, report_id=report_id)
    if not report:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    report = crud.update_report(
        db, report_obj=report, report_in=report_in
    )
    return report
