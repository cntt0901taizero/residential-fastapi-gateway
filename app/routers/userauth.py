import json
from typing import Union

import requests
from fastapi import APIRouter, Depends, Request, Header, Security, Body
from sqlalchemy.orm import Session

import app.schemas as Schemas
import app.services.auth_service as AuthService
import app.services.user_service as UserService
from app.services import auth_service, user_service
from configs import get_settings
from app.database import get_db
from app.repository import user_repo, token_repo
from app.schemas.user import User, LogoutSchema
from app.schemas.common import CommonResponse

router = APIRouter(
    prefix="/residential",
    tags=['Residential API']
)


@router.post('/auth/login')
async def login(request: Schemas.ResidentialLoginInput, db: Session = Depends(get_db)):
    try:
        url = get_settings().residential_server_url + '/api/authenticate/login'
        headers = {'Content-type': 'application/json'}
        json_obj = {
            "jsonrpc": "2.0",
            "params": {
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
        user = await user_service.get_user_change_pass(db, data['data']['id'])
        data['data']['mobile_change_password'] = user.mobile_change_password
        await token_repo.init_fcm_token(id=data['data']['id'], fcm_token=request.fcm_token, db=db)
        return data

    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)


@router.post('/auth/logout')
async def logout(
        data: LogoutSchema,
        sid: Union[str, None] = Header(default=None),
        user: User = Security(auth_service.auth_user),
        db: Session = Depends(get_db)
):
    try:
        url = get_settings().residential_server_url + '/api/authenticate/logout'
        cookies = {'session_id': sid}
        headers = {'Content-type': 'application/json', 'X-Openerp': sid}
        json_obj = {}
        rs = requests.post(url=url, json=json_obj, cookies=cookies, headers=headers)
        await token_repo.del_fcm_token(id=f"{user.id}", fcm_token=data.fcm_token, db=db)
        return CommonResponse.value(200, 'Logout Success', {})

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
        data: Schemas.ChangePassword,
        user: Schemas.User = Security(AuthService.auth_user),
        sid: str = Header(),
        db: Session = Depends(get_db)
):
    result = await UserService.change_password(data, sid, user, db)
    return CommonResponse.value(200, 'Success', result)


@router.get('/user')
async def get_user(
        user: User = Security(auth_service.auth_user),
        db: Session = Depends(get_db)
):
    result = await user_service.get_detail_user(db, user.id)
    return CommonResponse.value(200, 'Success', result)
