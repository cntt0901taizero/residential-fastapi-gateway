from sqlalchemy import Column, Integer, String, DateTime, Text

from app.database import Base


class News(Base):
    __tablename__ = 'tb_news'

    id = Column(Integer, primary_key=True, index=True)
    create_date = Column(DateTime)
    create_uid = Column(Integer)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
    name = Column(String)
    content = Column(Text)
    file_name = Column(String)
    news_description = Column(String)
    expired_date = Column(DateTime)
    status = Column(String)
    news_type = Column(String)
    blockhouse_id = Column(Integer)
    building_id = Column(Integer)

