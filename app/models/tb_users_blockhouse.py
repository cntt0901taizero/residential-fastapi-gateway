from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from app.database import Base


class UsersBlockhouse(Base):
    __tablename__ = 'tb_users_blockhouse_res_groups_rel'

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer)
    user_id = Column(Integer)
    job_title = Column(String)
    blockhouse_id = Column(Integer)
    building_id = Column(Integer)
    building_house_id = Column(Integer)
    owner = Column(Boolean)
    relationship_type = Column(String)
    user_group_code = Column(String)
    create_uid = Column(Integer)
    create_date = Column(DateTime)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
    building_floors_id = Column(Integer)
