from app.repository import complain_repo


async def add(db, data, user):
    complain = await complain_repo.add_new_complain(db, data, user)
    return complain

