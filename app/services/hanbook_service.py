from app.repository import handbook_repo, user_repo


async def get_user_handbook(db, user):
    handbook = await handbook_repo.get_user_handbook(db=db, user=user)
    return handbook
