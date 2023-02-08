import json

import requests
from fastapi import APIRouter, Depends, Request, Header, Security
from sqlalchemy.orm import Session

from config import get_settings
from src.repository.residential import user_repo
from src.repository.residential.fcm_token_repo import init_fcm_token, del_fcm_token
from src.schemas.residential import userauth_dto
from src.schemas.residential.common_dto import CommonResponse
from src.database import get_db
import src.services.UserService as UserService
import src.services.AuthService as AuthService
from src.schemas.User import ChangePassword, User

router = APIRouter(
    prefix="/residential",
    tags=['Residential API']
)


@router.post('/auth/login')
async def login(request: userauth_dto.ResidentialLoginInput, db: Session = Depends(get_db)):
    try:
        url = get_settings().residential_server_url + '/api/authenticate/login'
        headers = {'Content-type': 'application/json'}
        json_obj = {
            "jsonrpc": "2.0",
            "params": {
                # "db": 'odoo_db_dev',
                "login": request.login,
                "password": request.password
            }
        }
        rs = requests.post(url=url, json=json_obj, headers=headers)
        rs_json = json.loads(rs.text)
        if rs_json.get('status') != 200:
            return CommonResponse.value(rs_json.get('status'), rs_json.get('message'), None)
        header = (rs.headers.get('Set-Cookie')).split(';')
        data = json.loads(rs.text)
        data['data']['sid'] = str((header[0].split('='))[1])
        data['data']['expires_time'] = str((header[1].split('='))[1])
        await init_fcm_token(id=data['data']['id'], fcm_token=request.fcm_token, db=db)
        return data

    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)


@router.post('/auth/logout')
async def logout(fcm_token: str, request: Request, db: Session = Depends(get_db)):
    try:
        _sid = request.headers.get('sid')
        url = get_settings().residential_server_url + '/api/authenticate/logout'
        cookies = {'session_id': _sid}
        headers = {'Content-type': 'application/json', 'X-Openerp': _sid}
        json_obj = {}
        rs = requests.post(url=url, json=json_obj, cookies=cookies, headers=headers)
        await del_fcm_token(id=rs.get('data'), fcm_token=fcm_token, db=db)
        return json.loads(rs.text)

    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)


async def check_auth(sid: str):
    url = get_settings().residential_server_url + '/api/authenticate/check-auth'
    cookies = {'session_id': sid}
    headers = {'Content-type': 'application/json', 'X-Openerp': sid}
    json_obj = {}
    rs = requests.post(url=url, json=json_obj, cookies=cookies, headers=headers)
    return json.loads(rs.text)


@router.post('/user/get')
async def get_user(request: Request, db: Session = Depends(get_db)):
    try:
        _sid = request.headers.get('sid')
        check = await check_auth(_sid)
        if check.get('data') > 0:
            res = await user_repo.get_user_by_id(check.get('data'), db)
            return CommonResponse.value(200, 'Success', res)
        else:
            return CommonResponse.value(500, 'Error', None)

    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)


@router.post('/user/password')
async def change_password(
        data: ChangePassword,
        user: User = Security(AuthService.auth_user),
        sid: str = Header()
):
    try:
        result = await UserService.change_password(data, sid)
        return CommonResponse.value(200, 'Success', result)
    except Exception as e:
        return CommonResponse.value(500, 'Error', None)
