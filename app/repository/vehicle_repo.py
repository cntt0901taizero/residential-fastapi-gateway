import datetime

from sqlalchemy.orm import Session

from app import exceptions
from app.constants.common import Status
from app.models import Vehicle


async def register_vehicle(db: Session, user, house, data):
    try:
        vehicle = Vehicle(
            name=data.get('name'),
            vehicle_type=data.get("vehicle_type"),
            note=data.get('note'),
            status=Status.PENDING.name,
            blockhouse_id=house.blockhouse_id,
            building_id=house.building_id,
            building_house_id=house.id,
            user_id=user.id,
            create_date=datetime.datetime.now(),
            write_date=datetime.datetime.now(),
            license_plates=data.get('license_plates'),
            vehicle_color=data.get('vehicle_color'),
            vehicle_brand=data.get('vehicle_brand'),
            date_of_birth=data.get('date_of_birth'),
            phone=data.get('phone'),
            citizen_identification=data.get('citizen_identification'),
            relationship_type=data.get('relationship_type'),
        )
        db.add(vehicle)
        db.commit()
        db.refresh(vehicle)
        return vehicle
    except Exception as e:
        raise exceptions.QueryDataError(status_code=500, default_message=str(e))
