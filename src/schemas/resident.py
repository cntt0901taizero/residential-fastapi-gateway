from pydantic import BaseModel


class Resident(BaseModel):
    id: int
    name: str
    floor: int
    owner: str