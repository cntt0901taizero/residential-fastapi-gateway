from sqlalchemy import Column, Integer, String, Boolean, Float

from app.database import Base


class BuildingHouse(Base):
    __tablename__ = 'tb_building_house'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String)
    address = Column(String)
    area_apartment = Column(Float)
    house_type = Column(String)
    detail_description = Column(String)
    bedroom_number = Column(Integer)
    bathroom_number = Column(Integer)
    balcony_number = Column(Integer)
    building_floors_id = Column(Integer)
    building_id = Column(Integer)
    is_active = Column(Boolean)
    blockhouse_id = Column(Integer)
