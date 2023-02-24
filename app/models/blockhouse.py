from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.database import Base


class Blockhouse(Base):
    __tablename__ = 'tb_blockhouse'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String)
    description = Column(String)
    image = Column(String)
    address = Column(String)
    website = Column(String)
    phone = Column(String)
    local_link = Column(String)
    is_active = Column(Boolean)
