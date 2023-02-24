from sqlalchemy.orm import Session

from app import models


def get_building(db: Session, building_id: int):
    return db.query(models.Building).filter(models.BuildingHouse.id == building_id).first()