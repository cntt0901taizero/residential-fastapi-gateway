from typing import List, Optional
from pydantic import BaseModel


class GetByIdInput(BaseModel):
    id: Optional[int] = 0


class SearchPageInput(BaseModel):
    current_page: Optional[int] = 0
    page_size: Optional[int] = 10


class CommonResponse(BaseModel):
    @staticmethod
    def value(status: int, message: '', data: None):
        return {
            'status': status,
            'message': message,
            'data': data,
        }






