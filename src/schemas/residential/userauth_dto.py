from typing import List, Optional
from pydantic import BaseModel


class ResidentialLoginInput(BaseModel):
    login: str
    password: str
    fcmToken: str









