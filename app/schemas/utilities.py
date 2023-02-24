from typing import Optional

from pydantic import BaseModel



class RegisterDelivery(BaseModel):
    id: int
    blockhouse: str
    building: str
    name: str
    floor: int
    bloc_house: str
    status: Optional[int] = 500
