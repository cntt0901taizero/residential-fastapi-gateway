from pydantic import BaseModel

class BuildingHouseBase(BaseModel):
    name: str

class BuildingHouse(BaseModel):
    id: int