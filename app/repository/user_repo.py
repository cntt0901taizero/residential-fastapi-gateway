from sqlalchemy import text
from sqlalchemy.orm import Session

from app import exceptions
from configs import get_settings
from app.models import Users, UsersBlockhouse, BuildingHouse, Blockhouse, Building, Partner, UsersLog


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
        raise exceptions.QueryDataError(status_code=500, default_message=str(e))


async def get_full_info(db: Session, user_id):
    try:
        return db.query(
            Users.id,
            Users.user_type,
            Users.create_date,
            Users.gender,
            Users.citizen_identification,
            Partner.phone,
            Partner.display_name,
            Partner.email

        ) \
            .join(Partner, Partner.id == Users.partner_id) \
            .filter(Users.id == user_id) \
            .first()
    except Exception as e:
        raise exceptions.QueryDataError(status_code=500, default_message=str(e))


async def get_user_blockhouse(db: Session, user_id: int):
    try:
        return db.query(
            UsersBlockhouse.user_id.label("user_id"),
            UsersBlockhouse.owner.label('is_owner'),
            UsersBlockhouse.relationship_type.label('relationship_type'),

            Blockhouse.id.label("blockhouse_id"),
            Blockhouse.name.label("blockhouse_name"),
            Blockhouse.code.label("blockhouse_code"),
            Blockhouse.address.label("blockhouse_address"),

            Building.id.label('building_id'),
            Building.name.label('building_name'),
            Building.name_display.label('building_name_display'),
            Building.code.label('building_code'),

            BuildingHouse.id.label("house_id"),
            BuildingHouse.name.label("house_name"),
            BuildingHouse.name_display.label("house_name_display"),
            BuildingHouse.code.label("house_code"),
        ) \
            .join(Blockhouse, Blockhouse.id == UsersBlockhouse.blockhouse_id) \
            .join(Building, Building.id == UsersBlockhouse.building_id) \
            .join(BuildingHouse, BuildingHouse.id == UsersBlockhouse.building_house_id) \
            .filter(UsersBlockhouse.user_id == user_id) \
            .all()

    except Exception as e:
        raise exceptions.QueryDataError(status_code=500, default_message=str(e))


async def user_change_pass(db: Session, user_id: int):
    try:
        return db.query(Users.mobile_change_password).filter(Users.id == user_id).first()
    except Exception as e:
        raise exceptions.QueryDataError(status_code=500, default_message=str(e))


async def set_change_pass(db: Session, user_id: int):
    try:
        db.query(Users).filter(Users.id == user_id) \
            .update({Users.mobile_change_password: True})
        db.commit()
    except Exception as e:
        raise exceptions.QueryDataError(status_code=500, default_message=str(e))
