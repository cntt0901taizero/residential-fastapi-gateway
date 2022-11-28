from sqlalchemy.orm import Session
from src import database_odoo
from fastapi import Depends
from sqlalchemy import text

get_db = database_odoo.get_db


def get_user_by_id(uid: int, db: Session = Depends(get_db)):
    sql = text('select * from res_users where id = ' + str(uid))
    # result = (db.execute(sql)).fetchall()
    result = [dict(row) for row in db.execute(sql)]
    result[0]['password'] = ''
    return result


