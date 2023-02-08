from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session

from config import get_settings
import requests
import json
from src.database import get_db

from src.repository.residential import user_repo


async def get_login_data(sid: str):
    auth_url = get_settings().residential_server_url + '/api/authenticate/check-auth'
    cookies = {'session_id': sid}
    headers = {'Content-type': 'application/json', 'X-Openerp': sid}
    json_obj = {}
    rs = requests.post(url=auth_url, json=json_obj, cookies=cookies, headers=headers)
    return json.loads(rs.text)


async def auth_user(sid: str = Header(), db: Session = Depends(get_db)):
    if not sid:
        raise HTTPException(status_code=400, detail="sid header invalid")
    login_data = await get_login_data(sid)
    if not login_data.get('data'):
        raise HTTPException(status_code=400, detail="sid header invalid")
    user = await user_repo.get_user_detail(db, login_data.get('data'))
    return user
