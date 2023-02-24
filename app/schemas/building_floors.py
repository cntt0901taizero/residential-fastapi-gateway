from pydantic import BaseModel

class BuildingFloorsBase(BaseModel):
    name: str

class BuildingFloors(BaseModel):
    id: int