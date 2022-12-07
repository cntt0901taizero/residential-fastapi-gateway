from typing import List, Optional, Any
from pydantic import BaseModel


class GetByIdInput(BaseModel):
    id: Optional[int] = 0


class SearchPageInput(BaseModel):
    current_page: Optional[int] = 0
    page_size: Optional[int] = 10


class PageOutput(BaseModel):
    page_list_data: Optional[List] = []
    size: Optional[int] = 10
    total_pages: Optional[int] = 0
    total_items: Optional[int] = 0
    current_page: Optional[int] = 0


class CommonResponseOutputDto(BaseModel):
    status: Optional[int] = 500
    message: Optional[str] = ''
    data: Any = None


class CommonResponse(BaseModel):
    @staticmethod
    def value(status: int, message: '', data: None):
        return CommonResponseOutputDto(status=status, message=message, data=data)






