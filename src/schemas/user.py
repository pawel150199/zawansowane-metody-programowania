from typing import Optional, List
from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str = None
    last_name: str = None
    email: str = None


class CreateUser(UserBase):
    function: Optional[str]
    password: Optional[str]
    group_id: Optional[int]
    is_teamadmin: bool = False
    is_webadmin: bool = False



class CreateMember(UserBase):
    function: Optional[str]
    password: Optional[str]
    group_id: Optional[int]


class UpdateUser(UserBase):
    password: Optional[str]
    function: Optional[str]
    group_id: Optional[int]


class User(UserBase):
    id: int
    function: str
    group_id: Optional[int]
    is_teamadmin: bool
    is_webadmin: bool

    class Config:
        orm_mode = True


class UserWithId(User):
    id: int
