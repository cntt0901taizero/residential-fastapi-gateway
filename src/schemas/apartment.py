from typing import List

from pydantic import BaseModel

from src.schemas.resident import Resident


class Apartment(BaseModel):
    id: int
    code: str
    building: str
    name: str
    floor: int
    bloc_house: str
    residents: List[Resident]