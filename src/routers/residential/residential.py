from src import database_odoo
from src.routers.residential.userauth import check_auth
from src.schemas.residential import common_dto, news_dto
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from src.repository.residential import residential_repo
from src.schemas.residential.common_dto import CommonResponse
import requests
import json

router = APIRouter(
    prefix="/residential",
    tags=['Residential API']
)

get_db = database_odoo.get_db
residential_server = 'http://10.32.13.57:8069/'


@router.post('/news/search-page')
async def news_search_page(request: news_dto.NewsSearchPageInput, db: Session = Depends(get_db)):
    try:
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

    except Exception as e:
        return CommonResponse(500, 'Error', None)


@router.post('/notification/search-page')
async def notification_search_page(request: common_dto.SearchPageInput, db: Session = Depends(get_db)):
    try:
        check = await check_auth(request.sid)
        if check.get('data') > 0:
            res = residential_repo.search_notification_page(db)
            return CommonResponse.value(200, 'Success', res)
        else:
            return CommonResponse.value(500, 'Error', None)

    except Exception as e:
        return CommonResponse(500, 'Error', None)


@router.post('/banner/search-page')
async def banner_search_page(request: common_dto.SearchPageInput, db: Session = Depends(get_db)):
    try:
        check = await check_auth(request.sid)
        if check.get('data') > 0:
            res = residential_repo.search_banner_page(db)
            return CommonResponse.value(200, 'Success', res)
        else:
            return CommonResponse.value(500, 'Error', None)

    except Exception as e:
        return CommonResponse(500, 'Error', None)



