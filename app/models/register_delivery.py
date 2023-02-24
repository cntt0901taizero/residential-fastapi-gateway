from enum import Enum

from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.database import Base


class RegisterDelivery(Base):
    __tablename__ = 'tb_register_delivery'

    id = Column(Integer, primary_key=True, index=True)
    shipping_method = Column(Enum)
    through_method = Column(Enum)
    status = Column(Enum)
    freight_detail = Column(String)
    use_freight_elevator = Column(Boolean)
    blockhouse_id = Column(Integer)
    building_id = Column(Integer)
    building_house_id = Column(Integer)
    time_start = Column(DateTime)
    time_end = Column(DateTime)
