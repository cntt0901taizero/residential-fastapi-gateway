from pydantic import BaseModel

class BuildingBase(BaseModel):
    name: str

class Building(BaseModel):
    id: int