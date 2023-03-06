import datetime
from typing import Optional, List

from pydantic import BaseModel, validator

import configs


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


class LogoutSchema(BaseModel):
    fcm_token: str


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

    @validator("create_date")
    def convert_datetime(cls, create_date):
        return create_date.strftime(configs.get_settings().datetime_format) if create_date is not None else None

    class Config:
        orm_mode = True


class Handbook(BaseModel):
    id: int
    name: str
    image: Optional[str]
    create_date: datetime.datetime

    @validator("create_date")
    def convert_datetime(cls, create_date):
        return create_date.strftime(configs.get_settings().datetime_format) if create_date is not None else None

    class Config:
        orm_mode = True


class HandbookDetail(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    detail_description: Optional[str]
    image: Optional[str]
    create_date: datetime.datetime

    @validator("create_date")
    def convert_datetime(cls, create_date):
        return create_date.strftime(configs.get_settings().datetime_format) if create_date is not None else None

    class Config:
        orm_mode = True
