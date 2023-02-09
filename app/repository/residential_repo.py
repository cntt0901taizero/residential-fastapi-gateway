from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from configs import get_settings
from app.database import get_db
from app.models import UsersBlockhouse, ApartmentUtilities
import app.schemas as Schemas


async def get_user_by_id(uid: int, db: Session = Depends(get_db)):
    sql = text("select id, active, login, company_id, partner_id, "
               "create_date, signature, notification_type, phone_number "
               "from res_users where id = " + str(uid))
    result = [dict(row) for row in db.execute(sql)]
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


async def read_notification(id: int, db: Session):
    sql = text("update tb_push_notification "
               "set notification_status = 'SEEN' "
               "where id = " + str(id))
    rs = db.execute(sql)
    db.commit()
    return rs


async def search_notification_page(id: int, param: Schemas.SearchPageInput, db: Session = Depends(get_db),
                                   page_num: int = 0, page_size: int = 10):
    offset = count_offset(page_num, page_size)
    sql = text("select "
               "id, name, content, type, notification_status, create_date, write_date "
               "from tb_push_notification "
               "where user_id = " + str(id) + " "
                                              "order by id asc "
                                              f"limit {page_size} offset {offset}")
    result = [dict(row) for row in db.execute(sql)]
    return result


async def count_unread_notifications(id: int, db: Session):
    sql = text("select "
               "count(*)"
               "from tb_push_notification "
               "where user_id = " + str(id) + " "
                                              "and notification_status = 'SENT'")
    result = db.execute(sql).fetchone()
    return result


async def count_notifications(id: int, db: Session = Depends(get_db), ):
    sql = text("select "
               "count(*)"
               "from tb_push_notification "
               "where user_id = " + str(id))
    result = db.execute(sql).fetchone()
    return result.count


async def search_banner_page(param: Schemas.SearchPageInput, db: Session = Depends(get_db)):
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


async def get_user_block_house(user_id, db: Session):
    db: Session = get_db()
    return db.query(UsersBlockhouse.blockhouse_id) \
        .filter(UsersBlockhouse.user_id == user_id) \
        .all()


async def get_utilities_by_block_house_ids(block_house_ids, db: Session):
    query = db.query(ApartmentUtilities) \
        .filter(ApartmentUtilities.blockhouse_id.in_(block_house_ids)) \
        .filter(ApartmentUtilities.is_active.is_(True)) \
        .order_by(ApartmentUtilities.create_date.desc())

    return query.all(), query.count()
