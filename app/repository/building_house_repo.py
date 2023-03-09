from sqlalchemy.orm import Session

from app import exceptions
from app.models import BuildingHouse


async def get_house_info(db: Session, house_id):
    try:
        return db.query(BuildingHouse).filter(BuildingHouse.id == house_id).first()
    except Exception as e:
        raise exceptions.QueryDataError(status_code=500, default_message=str(e))
