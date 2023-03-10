from sqlalchemy import text
from sqlalchemy.orm import Session

from app.models.fcm_token import FcmToken


async def init_fcm_token(id: int, fcm_token: str, db: Session):
    exists = db.query(FcmToken.user_id).filter_by(name=fcm_token, user_id=id).first() is not None
    if not exists:
        new_record = FcmToken(name=fcm_token, user_id=id)
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        return new_record
    else:
        return


async def del_fcm_token(id: int, fcm_token: str, db: Session):
    sql = text(f"delete from tb_fcm_token where tb_fcm_token.name='{fcm_token}' and tb_fcm_token.user_id={id}")
    db.execute(sql)
    db.commit()
    return
