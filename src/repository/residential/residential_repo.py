from sqlalchemy.orm import Session
from src import database_odoo
from fastapi import Depends
from sqlalchemy import text
from config import get_settings
from src.schemas.residential import common_dto

get_db = database_odoo.get_db


async def get_user_by_id(uid: int, db: Session = Depends(get_db)):
    sql = text("select id, active, login, company_id, partner_id, "
               "create_date, signature, notification_type, phone_number "
               "from res_users where id = " + str(uid))
    # result = (db.execute(sql)).fetchall()
    result = [dict(row) for row in db.execute(sql)]
    # result[0]['password'] = ''
    return result

async def total(db: Session):
    sql = text("select id, name, "
               "concat('" + get_settings().residential_server_url +
               "', '/web/image?', 'model=tb_news&id=', id , '&field=image') as image_url, "
               "create_date, write_date, expired_date "
               "from tb_news where state = 'ACTIVE' "
               "order by id asc "
               )
    result = [dict(row) for row in db.execute(sql)]
    return len(result)

def count_offset(page_num: int, page_size: int):
    if page_num in (0, 1):
        offset = 0
    else:
        offset = (page_num * page_size) - page_size
    return offset

async def search_news_page(db: Session, page_num: int = 0, page_size: int = 100):
    offset = count_offset(page_num, page_size)
    sql = text("select id, name, "
               "concat('" + get_settings().residential_server_url +
               "', '/web/image?', 'model=tb_news&id=', id , '&field=image') as image_url, "
               "create_date, write_date, expired_date, content "
               "from tb_news where state = 'ACTIVE' "
               "order by id asc "
               f"limit {page_size} offset {offset}"
               )
    result = [dict(row) for row in db.execute(sql)]
    return result


async def get_news_detail(id: int, db: Session = Depends(get_db)):
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


async def search_notification_page(id: int, param: common_dto.SearchPageInput, db: Session = Depends(get_db),):
    sql = text("select "
               "id, name, content, type, notification_status, create_date, write_date "
               "from tb_push_notification "
               "where user_id = " + str(id) + " "
               "order by id asc "
               "limit " + str(param.page_size) + " offset " + str(param.page_size * param.current_page))
    result = [dict(row) for row in db.execute(sql)]
    return result


async def search_banner_page(param: common_dto.SearchPageInput, db: Session = Depends(get_db)):
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

