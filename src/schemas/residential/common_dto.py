from typing import List, Optional
from pydantic import BaseModel


class GetByIdInput(BaseModel):
    sid: Optional[str] = ''
    id: Optional[int] = 0


class CommonResponse(BaseModel):
    @staticmethod
    def value(status: int, message: '', data: None):
        return {
            'status': status,
            'message': message,
            'data': data,
        }






