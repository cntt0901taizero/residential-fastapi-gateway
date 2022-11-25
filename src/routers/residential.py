from src import database_odoo
from src.schemas import residential_dto
from src.models import fastapi_models
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import APIRouter, Depends, status
from src.repository import user, residential_repo
import requests
import json

router = APIRouter(
    prefix="/residential",
    tags=['Residential']
)

get_db = database_odoo.get_db
residential_server_ip = 'http://10.32.13.57:8069/'


@router.post('/auth/login')
async def login(request: residential_dto.ResidentialLoginInput):
    url = residential_server_ip + 'api/authenticate/login'
    json_obj = {
        "jsonrpc": "2.0",
        "params": {
            # "db": 'odoo_db_dev',
            "login": request.login,
            "password": request.password
        }
    }
    rs = requests.post(url=url, json=json_obj)
    if rs.status_code != 200:
        return {
            'status': rs.status_code,
            'message': 'Error',
            'data': []
        }
    header = (rs.headers.get('Set-Cookie')).split(';')
    data = json.loads(rs.text)
    data['data']['sid'] = str((header[0].split('='))[1])
    data['data']['expires_time'] = str((header[1].split('='))[1])
    return data


@router.post('/auth/logout')
def logout(session_id: str):
    url = residential_server_ip + 'api/authenticate/logout'
    cookies = {'session_id': session_id}
    headers = {'X-Openerp': session_id, 'Content-type': 'application/json'}
    json_obj = {}
    rs = requests.post(url=url, json=json_obj, cookies=cookies, headers=headers)
    return json.loads(rs.text)


@router.post('/user/get/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    res = residential_repo.get_user_by_id(id, db)
    return res


@router.post('/news/search-page')
def news_search_page(request: residential_dto.NewsSearchPageInput, db: Session = Depends(get_db)):
    url = residential_server_ip + 'api/news/search-page'
    json_obj = {
        "jsonrpc": "2.0",
        "params": {
             "current_page": request.current_page,
             "page_size": request.page_size
        }
    }
    rs = requests.post(url=url, json=json_obj)
    return json.loads(rs.text)
