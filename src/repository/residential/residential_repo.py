from sqlalchemy.orm import Session
from src import database_odoo
from fastapi import Depends
from sqlalchemy import text
from config import get_settings
from src.schemas.residential import common_dto


async def get_user_by_id(uid: int, db: Session):
    sql = text("select res_users.id, res_users.active, res_partner.name, res_partner.display_name, "
               "res_users.login, res_partner.lang, res_partner.tz, res_users.create_date, res_users.signature, "
               "res_partner.phone, res_partner.email, "
               "concat('" + get_settings().residential_server_url +
               "', '/web/image?', 'model=res.users&id=', res_users.id , '&field=avatar_1920') as image_url "
               "from res_users inner join res_partner on res_users.partner_id = res_partner.id "
               "where res_users.id = " + str(uid))
    # result = (db.execute(sql)).fetchall()
    result = [dict(row) for row in db.execute(sql)]
    # result[0]['password'] = ''
    return result


async def search_news_page(db: Session):
    sql = text("select id, name, "
               "concat('" + get_settings().residential_server_url +
               "', '/web/image?', 'model=tb_news&id=', id , '&field=image') as image_url, "
               "create_date, write_date, expired_date "
               "from tb_news where state = 'ACTIVE' "
               "order by id asc")
    result = [dict(row) for row in db.execute(sql)]
    return result


async def get_news_detail(id: int, db: Session):
    sql = text("select "
               "id, name, content, file_name, "
               "concat('" + get_settings().residential_server_url +
               "', '/web/image?', 'model=tb_news&id=', id , '&field=image') as image_url, "
               "concat('" + get_settings().residential_server_url +
               "', '/web/content/tb_news/', id , '/file') as file_url, "
               "create_date, write_date, expired_date "
               "from tb_news where id = " + str(id))
    result = [dict(row) for row in db.execute(sql)]
    # image_url = '/web/image?' + 'model=tb_news&id=' + str(
    #     item.id) + '&field=image' if item.image else None
    # file_url = '/web/content/tb_news/' + str(item.id) + '/file' if item.file else None
    return result


async def search_notification_page(id: int, param: common_dto.SearchPageInput, db: Session):
    sql = text("select "
               "id, name, content, type, notification_status, create_date, write_date "
               "from tb_push_notification "
               "where user_id = " + str(id) + " "
               "order by id asc "
               "limit " + str(param.page_size) + " offset " + str(param.page_size * param.current_page))
    result = [dict(row) for row in db.execute(sql)]
    return result


async def read_notification(id: int, db: Session):
    sql = text("update tb_push_notification "
               "set notification_status = 'SEEN' "
               "where id = " + str(id))
    rs = db.execute(sql)
    db.commit()
    return rs


async def search_banner_page(param: common_dto.SearchPageInput, db: Session):
    sql = text("select "
               "id, name, banner_description, "
               "concat('" + get_settings().residential_server_url +
               "', '/web/image?', 'model=tb_news&id=', id , '&field=image') as image_url, "
               "create_date, write_date "
               "from tb_banner "
               "order by create_date asc "
               "limit " + str(param.page_size) + " offset " + str(param.page_size * param.current_page))
    result = [dict(row) for row in db.execute(sql)]
    return result

