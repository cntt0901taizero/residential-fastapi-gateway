from typing import List, Optional
from pydantic import BaseModel


class NewsSearchPageInput(BaseModel):
    sid: Optional[str] = ''
    current_page: Optional[int] = 0
    page_size: Optional[int] = 10





