from typing import List

from pydantic import BaseModel

from app.schemas.resident import Resident


class Apartment(BaseModel):
    id: int
    code: str
    building: str
    name: str
    floor: int
    bloc_house: str
    residents: List[Resident]


class House(BaseModel):
    id: int
    name: str
    blockhouse_id: int
    building_id: int
    building_floors_id: int

    class Config:
        orm_mode = True
