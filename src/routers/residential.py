from src import database_odoo
from src.schemas.residential import common_dto, userauth_dto, news_dto
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from src.repository import residential_repo
import requests
import json

from src.schemas.residential.common_dto import CommonResponse

router = APIRouter(
    prefix="/residential",
    tags=['Residential']
)

get_db = database_odoo.get_db
residential_server = 'http://localhost:8069/'


@router.post('/auth/login')
async def login(request: userauth_dto.ResidentialLoginInput):
    try:
        url = residential_server + 'api/authenticate/login'
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
            return CommonResponse(rs_json.get('status'), rs_json.get('message'), None)
        header = (rs.headers.get('Set-Cookie')).split(';')
        data = json.loads(rs.text)
        data['data']['sid'] = str((header[0].split('='))[1])
        data['data']['expires_time'] = str((header[1].split('='))[1])
        return data

    except Exception as e:
        return CommonResponse(500, 'Error', None)


@router.post('/auth/logout')
async def logout(sid: str):
    url = residential_server + 'api/authenticate/logout'
    cookies = {'session_id': sid}
    headers = {'Content-type': 'application/json', 'X-Openerp': sid}
    json_obj = {}
    rs = requests.post(url=url, json=json_obj, cookies=cookies, headers=headers)
    return json.loads(rs.text)


@router.post('/auth/check-auth')
async def check_auth(sid: str):
    url = residential_server + 'api/authenticate/check-auth'
    cookies = {'session_id': sid}
    headers = {'Content-type': 'application/json', 'X-Openerp': sid}
    json_obj = {}
    rs = requests.post(url=url, json=json_obj, cookies=cookies, headers=headers)
    return json.loads(rs.text)


@router.post('/user/get')
async def get_user(sid: str, db: Session = Depends(get_db)):
    check = await check_auth(sid)
    if check.get('data') > 0:
        res = residential_repo.get_user_by_id(check.get('data'), db)
        return CommonResponse.value(200, 'Success', res)
    else:
        return CommonResponse.value(500, 'Error', None)


@router.post('/news/search-page')
async def news_search_page(request: news_dto.NewsSearchPageInput, db: Session = Depends(get_db)):
    url = residential_server + 'api/news/search-page'
    headers = {'Content-type': 'application/json'}
    json_obj = {
        "jsonrpc": "2.0",
        "params": {
            "current_page": request.current_page,
            "page_size": request.page_size
        }
    }
    rs = requests.post(url=url, json=json_obj, headers=headers)
    return json.loads(rs.text)


@router.post('/notification/search-page')
async def news_search_page(request: common_dto.SearchPageInput, db: Session = Depends(get_db)):
    check = await check_auth(request.sid)
    if check.get('data') > 0:
        res = residential_repo.search_notification_page(db)
        return CommonResponse.value(200, 'Success', res)
    else:
        return CommonResponse.value(500, 'Error', None)


@router.post('/banner/search-page')
async def news_search_page(request: common_dto.SearchPageInput, db: Session = Depends(get_db)):
    check = await check_auth(request.sid)
    if check.get('data') > 0:
        res = residential_repo.search_banner_page(db)
        return CommonResponse.value(200, 'Success', res)
    else:
        return CommonResponse.value(500, 'Error', None)

