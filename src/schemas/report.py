from typing import Optional

from pydantic import BaseModel


class ReportBase(BaseModel):
    title: Optional[str]


class UpdateReport(ReportBase):
    status: Optional[str]


class CreateReport(ReportBase):
    status: str
    user_id: int


class CreateMyReport(ReportBase):
    status: str


class Report(ReportBase):
    id: int
    status: str
    user_id: int

    class Config:
        orm_mode = True
