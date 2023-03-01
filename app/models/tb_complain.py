from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from app.database import Base


class Complain(Base):
    __tablename__ = 'tb_complain'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    content = Column(String)
    status_description = Column(String)
    user_id = Column(Integer)
    status = Column(String)
    blockhouse_id = Column(Integer)
    building_id = Column(Integer)
    building_house_id = Column(Integer)
    create_uid = Column(Integer)
    create_date = Column(DateTime, default=datetime.now)
    write_uid = Column(Integer)
    write_date = Column(DateTime, default=datetime.now, onupdate=datetime.now)

