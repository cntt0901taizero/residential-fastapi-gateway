import datetime
from typing import Optional

from pydantic import BaseModel


class ResidentialLoginInput(BaseModel):
    login: str
    password: str
    fcm_token: Optional[str] = None


class User(BaseModel):
    id: int
    sid: str
    email: str
    phone: str
    display_name: str


class ChangePassword(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str


class FullInfoUser(BaseModel):
    id: int
    user_type: Optional[str]
    create_date: Optional[datetime.datetime]
    gender: Optional[str]
    citizen_identification: Optional[int]
    date_of_birth: Optional[datetime.date]
    phone: Optional[str]
    display_name: Optional[str]
    email: Optional[str]

    class Config:
        orm_mode = True

