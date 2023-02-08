from src.repository.residential import residential_repo


async def get_list(params, user, db):
    block_house = await residential_repo.get_user_block_house(user_id=user.id, db=db)
    block_house_id = [b.blockhouse_id for b in block_house]
    return block_house
