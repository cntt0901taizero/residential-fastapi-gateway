from typing import List

from pydantic import parse_obj_as
from app.repository import delivery_repo
from app.schemas import SearchPageInput
from app.schemas.delivery import DeliveryOutSchema
from app.utilities import pagination
from app.utilities.pagination import parsing_pagination


async def register_delivery(db, user, house, data):
    delivery_detail = await delivery_repo.register_delivery(db, user, house, data)
    return delivery_detail


async def get_delivery(db, user, current_page, page_size, status):
    page_config = pagination.paging_config(current_page, page_size)
    data, total = await delivery_repo.list_delivery(db, user, page_config, status)
    data = parse_obj_as(List[DeliveryOutSchema], data)
    return parsing_pagination(data, total, SearchPageInput(current_page=current_page, page_size=page_size))
