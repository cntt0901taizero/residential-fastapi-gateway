from typing import List, Optional, Any

from humps.main import camelize
from pydantic import BaseModel


class PydanticModel(BaseModel):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True
        orm_mode = True


class GetByIdInput(BaseModel):
    id: Optional[int] = 0


class SearchPageInput(BaseModel):
    current_page: Optional[int] = 0
    page_size: Optional[int] = 10


class PageOutput(BaseModel):
    list_data: Optional[List] = []
    page_size: Optional[int] = 10
    total_pages: Optional[int] = 0
    total_items: Optional[int] = 0
    current_page: Optional[int] = 0


class CommonResponseOutputDto(BaseModel):
    status: Optional[int] = 500
    message: Optional[str] = ''
    data: Any = None


class Paging(BaseModel):
    limit: Optional[int] = 10
    offset: Optional[int] = 0


class CommonResponse:
    @staticmethod
    def value(status: int, message: '', data: None):
        return CommonResponseOutputDto(status=status, message=message, data=data)
