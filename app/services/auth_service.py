import json

import requests
from fastapi import Header, Depends
from fastapi.security import SecurityScopes
from sqlalchemy.orm import Session

from app.database import get_db
from app import exceptions
from app.repository import user_repo
from configs import get_settings


async def get_login_data(sid: str):
    try:
        auth_url = get_settings().residential_server_url + '/api/authenticate/check-auth'
        cookies = {'session_id': sid}
        headers = {'Content-type': 'application/json', 'X-Openerp': sid}
        json_obj = {}
        rs = requests.post(url=auth_url, json=json_obj, cookies=cookies, headers=headers)
        return json.loads(rs.text)
    except Exception as e:
        raise exceptions.APIAuthenticationError(status_code=400, default_message="Không thể gọi tới api check quyền")


async def auth_user(
        security_scopes: SecurityScopes,
        sid: str = Header(),
        db: Session = Depends(get_db)
):
    if not sid:
        raise exceptions.InvalidCredentials(status_code=400, default_message="sid không được trống")
    login_data = await get_login_data(sid)
    if not login_data.get('data'):
        raise exceptions.InvalidCredentials(status_code=400, default_message="Phiên đăng nhập hết hạn")
    user = await user_repo.get_user_detail(db, login_data.get('data'))
    return user
