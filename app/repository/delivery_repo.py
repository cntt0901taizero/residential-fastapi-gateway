import datetime

from sqlalchemy.orm import Session

from app.constants.common import Status
from app.models.tb_register_delivery import RegisterDelivery
from app import exceptions


async def register_delivery(db: Session, user, house, data):
    try:
        delivery = RegisterDelivery(
            shipping_method=data.shipping_method,
            through_method=data.through_method,
            time_start=data.time_start,
            time_end=data.time_end,
            freight_detail=data.freight_detail,
            use_freight_elevator=data.use_freight_elevator,
            status=Status.PENDING.name,
            blockhouse_id=house.blockhouse_id,
            building_id=house.building_id,
            building_house_id=house.id,
            create_uid=user.id,
            create_date=datetime.datetime.now()
        )
        db.add(delivery)
        db.commit()
        db.refresh(delivery)
        return delivery
    except Exception as e:
        raise exceptions.QueryDataError(status_code=500, default_message=str(e))


async def list_delivery(db: Session, user, paging, status=None):
    try:
        query = db.query(RegisterDelivery) \
            .filter(RegisterDelivery.create_uid == user.id) \
            .order_by(RegisterDelivery.create_date.desc())
        if status:
            query = query.filter(RegisterDelivery.status == status)

        total_item = query.count()
        data = query.limit(paging.limit).offset(paging.offset).all()
        return data, total_item
    except Exception as e:
        raise exceptions.QueryDataError(status_code=500, default_message=str(e))


async def get_delivery_by_id(db, user, delivery_id):
    try:
        return db.query(RegisterDelivery).filter(RegisterDelivery.create_uid == user.id) \
            .filter(RegisterDelivery.id == delivery_id) \
            .first()
    except exceptions as e:
        raise exceptions.QueryDataError(status_code=500, default_message=str(e))
