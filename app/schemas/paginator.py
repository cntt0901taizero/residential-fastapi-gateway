from typing import List

from pydantic import BaseModel


class MetaPaginator(BaseModel):
    previous: bool
    next: bool


class Paginator(BaseModel):
    data: List[dict]
    total: int
    count: int
    pagination: MetaPaginator
