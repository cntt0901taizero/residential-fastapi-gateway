from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.database import Base


class Banner(Base):
    __tablename__ = 'tb_banner'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    banner_description = Column(String)
    link = Column(String)
    sort = Column(Integer)
    status = Column(String)
    blockhouse_id = Column(Integer)
    create_uid = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
