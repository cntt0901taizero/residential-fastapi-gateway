from sqlalchemy.orm import Session

from app import models


def get_building_floors(db: Session, building_floors_id: int):
    return db.query(models.BuildingFoors).filter(models.BuildingHouse.id == building_floors_id).first()