from sqlalchemy.orm import Session

from app.constants.common import NewsStatus
from app.models.tb_news import News


async def get_list(db: Session, paging):
    query = db.query(News) \
        .filter(News.status == NewsStatus.ACTIVE.name) \
        .order_by(News.create_date.desc())
    total_item = query.count()
    data = query.limit(paging.limit).offset(paging.offset).all()
    return data, total_item
