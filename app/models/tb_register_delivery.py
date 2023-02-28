from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from app.database import Base


class RegisterDelivery(Base):
    __tablename__ = 'tb_register_delivery'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    shipping_method = Column(String)
    through_method = Column(String)
    time_start = Column(DateTime)
    time_end = Column(DateTime)
    freight_detail = Column(String)
    use_freight_elevator = Column(Boolean)
    status = Column(String)
    blockhouse_id = Column(String)
    building_id = Column(Integer)
    building_house_id = Column(Integer)
    user_id = Column(Integer)
    create_uid = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
