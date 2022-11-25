from sqlalchemy.orm import Session
from src import database_odoo
from src.schemas import residential_dto
from fastapi import HTTPException, APIRouter, status, Depends
from src.service.hashing import Hash
from sqlalchemy import text

get_db = database_odoo.get_db


def get_user_by_id(id: int, db: Session = Depends(get_db)):
    sql = text('select * from res_users where id = ' + str(id))
    # result = (db.execute(sql)).fetchall()
    result = [dict(row) for row in db.execute(sql)]
    result[0]['password'] = ''
    return result


