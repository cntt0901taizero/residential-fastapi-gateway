from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float
from app.database import Base


class Building(Base):
    __tablename__ = 'tb_building'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    name_display = Column(String)
    code = Column(String)
    address = Column(String)
    founding_date = Column(DateTime)
    website = Column(String)
    phone = Column(String)
    location_link = Column(String)
    building_level = Column(String)
    is_active = Column(Boolean)
    blockhouse_id = Column(Integer)
    create_uid = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
