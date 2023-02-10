from app.repository.residential_repo import get_user_block_house, get_utilities_by_block_house_ids
from app.utilities.pagination import parsing_pagination, get_paging_config
from app.utilities.common import get_data_image


async def get_list(db, request, user):
    block_house = await get_user_block_house(user_id=user.id, db=db)
    block_house_id = set([b.blockhouse_id for b in block_house])

    paging_config = get_paging_config(request)
    data, total = await get_utilities_by_block_house_ids(
        db=db,
        block_house_ids=block_house_id,
        paging=paging_config
    )
    data = get_data_image(data, 'tb_apartment_utilities')
    return parsing_pagination(data, total, request)


