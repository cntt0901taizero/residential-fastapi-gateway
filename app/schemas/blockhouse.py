from pydantic import BaseModel

class BlockHouseBase(BaseModel):
    name: str

class BlockHouse(BaseModel):
    id: int