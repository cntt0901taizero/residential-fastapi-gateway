from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.database import Base


class UsersLog(Base):
    __tablename__ = 'res_users_log'

    id = Column(Integer, primary_key=True, index=True)
    create_uid = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
