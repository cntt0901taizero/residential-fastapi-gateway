from sqlalchemy.orm import Session

from app.constants.common import ComplainStatus
from app.models.tb_complain import Complain
from app.utilities.upload import upload_image


async def add_new_complain(db: Session, data, user):
    try:
        complain = Complain(name=data.get('name'),
                            content=data.get('content'),
                            blockhouse_id=data.get('blockhouse_id'),
                            building_id=data.get('building_id'),
                            status=ComplainStatus.PENDING.name,
                            user_id=user.id)
        db.add(complain)
        db.commit()
        db.refresh(complain)
        await upload_image(data.get('image'), 'tb_complain', complain.id)
        return complain
    except Exception as e:
        return e


async def get_list(db: Session, filter_data, paging, user):
    try:
        query = db.query(Complain) \
            .filter(Complain.status == filter_data.get('status')) \
            .filter(Complain.user_id == user.id) \
            .order_by(Complain.create_date.desc())
        total = query.count()
        data = query.limit(paging.limit).offset(paging.offset).all()
        return data, total
    except Exception as e:
        return e
