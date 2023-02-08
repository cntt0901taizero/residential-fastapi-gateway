from sqlalchemy import Column, Integer, String, ForeignKey
from src.database import Base
from sqlalchemy.orm import relationship


class FcmToken(Base):
    __tablename__ = 'tb_fcm_token'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
