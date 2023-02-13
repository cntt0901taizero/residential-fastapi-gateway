from app.repository import complain_repo
from app.utilities.common import get_data_image
from app.utilities.pagination import get_paging_config, parsing_pagination
from app.schemas.common import SearchPageInput


async def add(db, data, user):
    complain = await complain_repo.add_new_complain(db, data, user)
    return complain


async def get_list(db, filter_data, user):
    search_input = SearchPageInput(current_page=filter_data.get('current_page'),page_size=filter_data.get('page_size'))
    paging_config = get_paging_config(search_input)
    data, total = await complain_repo.get_list(db, filter_data, paging_config, user)
    data = get_data_image(data, 'tb_complain')

    return parsing_pagination(data, total, search_input)
