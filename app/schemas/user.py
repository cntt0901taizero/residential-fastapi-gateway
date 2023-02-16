from typing import Optional, List

from pydantic import BaseModel
from pydantic.schema import datetime


class ResidentialLoginInput(BaseModel):
    login: str
    password: str
    fcm_token: Optional[str] = None


class User(BaseModel):
    id: int
    login: str
    phone_number: Optional[str]
    user_type: Optional[str]
    gender: Optional[str]
    blockhouse_ids: Optional[List[int]]
    building_ids: Optional[List[int]]


class ChangePassword(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str
