from sqlalchemy.orm import Session

from app.models import BuildingHouse


async def get_house_info(db: Session, house_id):
    try:
        return db.query(BuildingHouse).filter(BuildingHouse.id == house_id).first()
    except Exception as e:
        return e
