from typing import List

from pydantic import parse_obj_as

from app.repository.residential_repo import get_handbooks_by_block_house_ids, get_handbook_detail
from app.schemas import Handbook, HandbookDetail
from app.utilities.common import get_data_image
from app.utilities.pagination import parsing_pagination, get_paging_config
from configs import get_settings


async def get_list(db, request, house):
    try:
        paging_config = get_paging_config(request)
        data, total = await get_handbooks_by_block_house_ids(
            db=db,
            house=house,
            paging=paging_config
        )
        data = parse_obj_as(List[Handbook], data)
        data = get_data_image(data, 'tb_resident_handbook')
        return parsing_pagination(data, total, request)
    except Exception as e:
        return e


async def get_detail(db, handbook_id):
    try:
        data = await get_handbook_detail(db, handbook_id)
        data = HandbookDetail.from_orm(data)
        data.image = f"{get_settings().residential_server_url}/web/image?model=tb_resident_handbook&id={data.id}&field=image"
        return data
    except Exception as e:
        return e
