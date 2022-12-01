from sqlalchemy.orm import Session

from src.models.fcm_token_model import FcmToken
from src.schemas import fastapi_dto

def init_fcm_token(request: fastapi_dto.FcmToken, db: Session):
    exists = db.query(FcmToken.user_id).filter_by(name=request.fcm_token, user_id=request.user_id).first() is not None
    if not exists:
        new_record = FcmToken(name=request.fcm_token, user_id=request.user_id)
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        return new_record
    else:
        return
