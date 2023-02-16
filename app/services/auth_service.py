import json
import requests
from fastapi import Header, HTTPException, Depends
from fastapi.security import SecurityScopes
from sqlalchemy.orm import Session
from configs import get_settings
from app.database import get_db
from app.repository import user_repo
from app.schemas.user import User


async def get_login_data(sid: str):
    auth_url = get_settings().residential_server_url + '/api/authenticate/check-auth'
    cookies = {'session_id': sid}
    headers = {'Content-type': 'application/json', 'X-Openerp': sid}
    json_obj = {}
    rs = requests.post(url=auth_url, json=json_obj, cookies=cookies, headers=headers)
    return json.loads(rs.text)


async def auth_user(
        security_scopes: SecurityScopes,
        sid: str = Header(),
        db: Session = Depends(get_db)
):
    if not sid:
        raise HTTPException(status_code=400, detail="sid header invalid")
    login_data = await get_login_data(sid)
    if not login_data.get('data'):
        raise HTTPException(status_code=400, detail="sid header invalid")
    user = await user_repo.get_user_detail(db, login_data.get('data'))

    user_data = await user_repo.get_user_block_house_building(db, user_id=user.id)
    user_blockhouse = set([item.blockhouse_id for item in user_data])
    user_building = set([item.building_id for item in user_data])

    return User(
        id=user.id,
        login=user.login,
        phone_number=user.phone_number,
        date_of_birth=user.date_of_birth,
        gender=user.gender,
        user_type=user.user_type,
        blockhouse_ids=user_blockhouse,
        building_ids=user_building
    )
