from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float
from app.database import Base


class BuildingHouse(Base):
    __tablename__ = 'tb_building_house'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String)
    address = Column(String)
    house_type = Column(String)
    area_apartment = Column(Float)
    bedroom_number = Column(Integer)
    bathroom_number = Column(Integer)
    balcony_number = Column(Integer)
    fee_base = Column(Float)
    detailed_description = Column(String)
    is_active = Column(Boolean)
    blockhouse_id = Column(Integer)
    building_id = Column(Integer)
    building_floors_id = Column(Integer)
    create_uid = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
