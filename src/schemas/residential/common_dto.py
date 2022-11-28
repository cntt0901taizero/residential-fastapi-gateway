from typing import List, Optional
from pydantic import BaseModel


class GetByIdInput(BaseModel):
    sid: Optional[str] = ''
    id: Optional[int] = 0


class SearchPageInput(BaseModel):
    sid: Optional[str] = ''
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






