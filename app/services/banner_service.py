from app.repository import banner_repo
from app.utilities.common import get_data_image
from app.utilities.pagination import get_paging_config, parsing_pagination, paging_config
from app.schemas.common import SearchPageInput


async def get_list(db, current_page, page_size, user):
    page_config = paging_config(current_page, page_size)
    data, total = await banner_repo.get_list(db, page_config, user)
    data = get_data_image(data, 'tb_banner')
    return parsing_pagination(data, total, SearchPageInput(current_page=current_page, page_size=page_size))

    return data
