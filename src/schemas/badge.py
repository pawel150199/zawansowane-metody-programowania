from typing import List

from pydantic import BaseModel


class BadgeGroup(BaseModel):
    group: str

    class Config:
        orm_mode = True


class BadgeBase(BaseModel):
    name: str
    description: List[str]

    class Config:
        orm_mode = True


class BadgeBaseWithId(BadgeBase):
    id: int

    class Config:
        orm_mode = True


class CreateBadge(BadgeBase):
    group: str


class Badge(BadgeBase):
    group: str

    class Config:
        orm_mode = True


class BadgeAll(BaseModel):
    group: str
    badges: List[BadgeBase]

    class Config:
        orm_mode = True
