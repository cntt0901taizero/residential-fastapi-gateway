from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.database import Base


class ApartmentUtilities(Base):
    __tablename__ = 'tb_apartment_utilities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    name_display = Column(String)
    description = Column(String)
    detail_description = Column(String)
    is_active = Column(Boolean)
    blockhouse_id = Column(Integer)
    create_uid = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)