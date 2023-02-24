from sqlalchemy.orm import Session

from app import models


def get_building_house(db: Session, building_house_id: int):
    return db.query(models.BuildingHouse).filter(models.BuildingHouse.id == building_house_id).first()