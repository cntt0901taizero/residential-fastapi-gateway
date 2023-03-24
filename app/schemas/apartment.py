import datetime
from typing import List

from pydantic import BaseModel, validator

import configs
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

    @validator("time_start", "time_end", each_item=True)
    def convert_datetime(cls, v):
        return datetime.datetime.strptime(v, configs.get_settings().datetime_format)


class VehicleIn(BaseModel):
    name: str
    vehicle_type: str
    license_plates: str = None
    vehicle_color: str
    vehicle_brand: str
    date_of_birth: str
    phone: str
    citizen_identification: int
    relationship_type: str

    @validator('date_of_birth')
    def convert_datetime(cls, v):
        return datetime.datetime.strptime(v, configs.get_settings().date_format).date()

    @validator('relationship_type')
    def relationship_type_validate(cls, v):
        assert v in ['chuho', 'ongba', 'bome', 'vochong', 'concai', 'anhchiem',
                     'nguoithue'], 'Phải là 1 trong các type chuho, ongba, bome, vochong, concai, anhchiem, nguoithue '
        return v

    @validator('vehicle_type')
    def vehicle_type_validate(cls, v):
        assert v in ['bicycle', 'motorbike', 'car'], 'Phải là 1 trong các type bicycle, motorbike, car'
        return v
