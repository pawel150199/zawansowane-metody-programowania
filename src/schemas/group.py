from typing import Optional

from pydantic import BaseModel


class GroupBase(BaseModel):
    name: Optional[str]


class CreateGroup(GroupBase):
    wydzial: str
    uczelnia: str


class UpdateGroup(GroupBase):
    wydzial: Optional[str]
    uczelnia: Optional[str]


class Group(GroupBase):
    id: int
    wydzial: str
    uczelnia: str

    class Config:
        orm_mode = True
