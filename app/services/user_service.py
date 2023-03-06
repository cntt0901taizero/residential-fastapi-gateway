import requests
import json

from sqlalchemy.orm import Session

from app.repository import user_repo
from app.schemas import FullInfoUser
from app.utilities.common import get_data_image
from configs import get_settings


async def change_password(data, sid):
    auth_url = get_settings().residential_server_url + '/api/users/update_password'
    cookies = {'session_id': sid}
    headers = {'Content-type': 'application/json', 'X-Openerp': sid}
    json_obj = {
        "jsonrpc": "2.0",
        "params": {
            "old": data.old_password,
            "new1": data.new_password,
            "new2": data.confirm_password,

        }
    }
    rs = requests.post(url=auth_url, json=json_obj, cookies=cookies, headers=headers)
    return json.loads(rs.text)


async def get_detail_user(db: Session, user_id):
    try:
        user_detail = await user_repo.get_full_info(db, user_id)
        user_detail = FullInfoUser.from_orm(user_detail).dict()
        user_detail['image'] = f"{get_settings().residential_server_url}/web/image?model=res.users" \
                               f"&id={user_detail.get('id')}&field=avatar_1920"
        user_block_house = await user_repo.get_user_blockhouse(db, user_id)
        user_detail['block_house'] = user_block_house
        return user_detail
    except Exception as e:
        return e


async def count_user_login(db: Session, user_id):
    try:
        login_time = await user_repo.count_user_login(db, user_id)
        return login_time
    except Exception as e:
        return e
