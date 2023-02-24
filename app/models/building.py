from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.database import Base


class Building(Base):
    __tablename__ = 'tb_building'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String)
    founding_date = Column(DateTime)
    image = Column(String)
    address = Column(String)
    website = Column(String)
    phone = Column(String)
    local_link = Column(String)
    building_level = Column(String)
    is_active = Column(Boolean)
    blockhouse_id = Column(Integer)
    apartment_utilities_id = Column(Integer)
