from src import database_odoo
from src.routers.residential.userauth import check_auth
from src.schemas.residential import common_dto, news_dto
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Request
from src.repository.residential import residential_repo
from src.schemas.residential.common_dto import CommonResponse
from config import get_settings
import requests
import json

router = APIRouter(
    prefix="/residential",
    tags=['Residential API']
)

get_db = database_odoo.get_db


@router.post('/news/search-page')
async def news_search_page(param: news_dto.NewsSearchPageInput, db: Session = Depends(get_db)):
    try:
        url = get_settings().residential_server_url + '/api/news/search-page'
        headers = {'Content-type': 'application/json'}
        json_obj = {
            "jsonrpc": "2.0",
            "params": {
                "current_page": param.current_page,
                "page_size": param.page_size
            }
        }
        rs = requests.post(url=url, json=json_obj, headers=headers)
        return json.loads(rs.text)

    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)


@router.post('/notification/search-page')
async def notification_search_page(param: common_dto.SearchPageInput,
                                   request: Request, db: Session = Depends(get_db)):
    try:
        _sid = request.headers.get('sid')
        check = await check_auth(_sid)
        if check.get('data') > 0:
            res = residential_repo.search_notification_page(db)
            return CommonResponse.value(200, 'Success', res)
        else:
            return CommonResponse.value(500, 'Error', None)

    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)


@router.post('/banner/search-page')
async def banner_search_page(request: Request, db: Session = Depends(get_db)):
    try:
        _sid = request.headers.get('sid')
        check = await check_auth(_sid)
        if check.get('data') > 0:
            res = residential_repo.search_banner_page(db)
            return CommonResponse.value(200, 'Success', res)
        else:
            return CommonResponse.value(500, 'Error', None)

    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)



