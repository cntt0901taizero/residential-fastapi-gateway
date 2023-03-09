import datetime
from typing import List

from pydantic import BaseModel, validator

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


class RegisterDelivery(BaseModel):
    shipping_method: str
    through_method: str
    time_start: str
    time_end: str
    freight_detail: str
    use_freight_elevator: bool
