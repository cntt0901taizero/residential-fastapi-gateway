from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float
from app.database import Base


class Blockhouse(Base):
    __tablename__ = 'tb_blockhouse'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String)
    investor_name = Column(String)
    address = Column(String)
    website = Column(String)
    phone = Column(String)
    location_link = Column(String)
    is_active = Column(Boolean)
    create_uid = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
