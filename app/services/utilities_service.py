from app.repository.residential_repo import get_user_block_house, get_utilities_by_block_house_ids


async def get_list(request, user, db):
    block_house = await get_user_block_house(user_id=user.id, db=db)
    block_house_id = set([b.blockhouse_id for b in block_house])

    data, count = await get_utilities_by_block_house_ids(
        block_house_ids=block_house_id, db=db
    )

    return data
