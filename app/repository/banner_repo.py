from sqlalchemy.orm import Session

from app import exceptions
from app.constants.common import NewsStatus
from app.models.tb_banner import Banner
from app.utilities.upload import upload_image


async def get_list(db: Session, page_config, user):
    try:
        query = db.query(Banner) \
            .filter(Banner.status == NewsStatus.ACTIVE.name) \
            .order_by(Banner.create_date.desc())
        total = query.count()
        data = query.limit(page_config.limit).offset(page_config.offset).all()
        return data, total
    except Exception as e:
        raise exceptions.QueryDataError(status_code=500, default_message=str(e))
