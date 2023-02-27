from sqlalchemy.orm import Session

from app.constants.common import NewsStatus
from app.models.tb_news import News
from app.repository import news_repo
from app.utilities.common import get_data_image
from app.utilities.pagination import get_paging_config, parsing_pagination
from app.schemas.common import SearchPageInput


async def get_list(db: Session, paging):
    data, total = await news_repo.get_list(db, paging)
    data = get_data_image(data, 'tb_news')
    return parsing_pagination(data, total, SearchPageInput(current_page=1,page_size=10))
