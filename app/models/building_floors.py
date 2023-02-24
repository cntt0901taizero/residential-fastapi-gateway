from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.database import Base


class BuildingFloors(Base):
    __tablename__ = 'tb_building_floors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sort = Column(Integer)
    total_house = Column(Integer)
    floors_type = Column(String)
    building_id = Column(Integer)
    is_active = Column(Boolean)
    blockhouse_id = Column(Integer)