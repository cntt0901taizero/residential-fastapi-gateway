from sqlalchemy import text
from sqlalchemy.orm import Session

from configs import get_settings
from app.models.res_users import Users


async def get_user_by_id(uid: int, db: Session):
    sql = text("select res_users.id, res_users.active, res_partner.name, res_partner.display_name, "
               "res_users.login, res_partner.lang, res_partner.tz, res_users.create_date, res_users.signature, "
               "res_partner.phone, res_partner.email, "
               "concat('" + get_settings().residential_server_url +
               "', '/web/image?', 'model=res.users&id=', res_users.id , '&field=avatar_1920') as image_url "
               "from res_users inner join res_partner on res_users.partner_id = res_partner.id "
               "where res_users.id = " + str(uid))
    result = [dict(row) for row in db.execute(sql)]
    return result[0]


async def get_user_detail(db: Session, user_id: int):
    try:
        return db.query(Users).filter(Users.id == user_id).first()
    except Exception as e:
        return False
