from sqlalchemy.orm import Session
from src.schemas import fastapi_dto
from src.models import fastapi_models
from src.models import fcm_token_model
from fastapi import HTTPException, status
from src.hashing import Hash


def create(request: fastapi_dto.User, db: Session):
    new_user = fastapi_models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def init_fcm_token(request: fastapi_dto.FcmToken, db: Session):
    new_record = fcm_token_model.FcmToken(name=request.fcm_token, user_id= request.user_id)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

def show(id: int, db: Session):
    user = db.query(fastapi_models.User).filter(fastapi_models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user
