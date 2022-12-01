from sqlalchemy.orm import Session

from src import database_odoo
from src.models.fcm_token_model import FcmToken
from fastapi import Depends
from sqlalchemy import text

get_db = database_odoo.get_db


def init_fcm_token(id: int, fcm_token: str, db: Session = Depends(get_db)):
    exists = db.query(FcmToken.user_id).filter_by(name=fcm_token, user_id=id).first() is not None
    if not exists:
        new_record = FcmToken(name=fcm_token, user_id=id)
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        return new_record
    else:
        return


def del_fcm_token(id: int, fcm_token: str, db: Session = Depends(get_db)):
    sql = text("delete from tb_fcm_token where name=" + fcm_token + " and user_id=" + id)
    db.execute(sql)
    return None
