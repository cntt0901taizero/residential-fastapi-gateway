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
