from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from app.database import Base


class Vehicle(Base):
    __tablename__ = 'tb_vehicle'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    vehicle_type = Column(String)
    note = Column(String)
    status = Column(String)
    blockhouse_id = Column(Integer)
    building_id = Column(Integer)
    building_house_id = Column(Integer)
    user_id = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
    license_plates = Column(String)
    vehicle_color = Column(String)
    vehicle_brand = Column(String)
    date_of_birth = Column(Date)
    phone = Column(String)
    citizen_identification = Column(Integer)
    relationship_type = Column(String)
