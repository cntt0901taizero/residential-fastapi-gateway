from typing import List, Optional
from pydantic import BaseModel, BaseSettings


class ResidentialLoginInput(BaseModel):
    login: str
    password: str









