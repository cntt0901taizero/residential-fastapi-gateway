from typing import List, Optional
from pydantic import BaseModel


class NewsSearchPageInput(BaseModel):
    current_page: Optional[int] = 0
    page_size: Optional[int] = 10





