from sqlalchemy import Column, Integer, String

from app.database import Base


class FcmToken(Base):
    __tablename__ = 'tb_fcm_token'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
