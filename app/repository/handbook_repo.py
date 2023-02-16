from sqlalchemy.orm import Session
from app.models.tb_resident_handbook import ResidentHandbook
from app.models.tb_users_blockhouse import UsersBlockhouse

async def get_user_handbook(db: Session, user):
    return db.query(ResidentHandbook).all()
