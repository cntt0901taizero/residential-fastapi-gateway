import datetime
from typing import Union

from pydantic import BaseModel, validator

import configs


class DeliveryOutSchema(BaseModel):
    id: int
    name: Union[str]
    shipping_method: Union[str]
    through_method: Union[str]
    time_start: datetime.datetime
    time_end: datetime.datetime
    freight_detail: str
    use_freight_elevator: bool
    create_date: datetime.datetime
    status: str

    @validator("create_date", "time_start", "time_end", each_item=True)
    def convert_datetime(cls, v):
        return v.strftime(configs.get_settings().datetime_format) if v is not None else None


    class Config:
        orm_mode = True
