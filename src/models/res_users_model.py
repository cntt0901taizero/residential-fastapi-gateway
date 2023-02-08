from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from src.database import Base


class ResUsers(Base):
    __tablename__ = 'res_users'

    id = Column(Integer, primary_key=True, index=True)
    active = Column(Boolean, default=True)
    login = Column(String)
    password = Column(String, nullable=False)
    company_id = Column(Integer, nullable=False)
    partner_id = Column(Integer, nullable=False)
    create_date = Column(DateTime)
    signature = Column(String)
    action_id = Column(Integer)
    share = Column(Boolean)
    create_uid = Column(Integer)
    write_uid = Column(Integer)
    write_date = Column(DateTime)
    totp_secret = Column(String)
    notification_type = Column(String)
    odoobot_state = Column(String)
    odoobot_failed = Column(Boolean)
    phone_number = Column(String)
    citizen_identification = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    user_type = Column(String)
