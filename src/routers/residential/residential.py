from typing import List

from src import database_odoo
from src.repository.Paginate import paginate
from src.routers.residential.userauth import check_auth
from src.schemas.apartment import Apartment
from src.schemas.resident import Resident
from src.schemas.residential import common_dto, news_dto
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Request
from fastapi import APIRouter, Path, Query
from starlette import status as http_status
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


@router.get("/apartments", response_model=List[Apartment])
async def get_apartments():
    aparments = []
    for i in range(1, 5):
        residents = []
        for j in range(1,3):
            resident = Resident(
                id=j,
                name="Khai AB1",
                image="https://m.media-amazon.com/images/I/61EAm1WvFvL._AC_SX425_.jpg"
            )
            residents.append(resident)
        apartment = Apartment(
            id=i,
            code=f"Room {i}",
            building="AnBinhA3",
            name="12020",
            floor=12,
            bloc_house="AB18",
            residents=residents,
        )
        aparments.append(apartment)
    return aparments
@router.get(
    "/residents/{id}",
    response_model=Resident,
    status_code=http_status.HTTP_200_OK,
)

async def get_resident(id: int = Path(title="Room ID")):
    resident = Resident(
        id=id,
        code="A2010",
        building="An Binh City A3",
        name="2010",
        bloc_house="ABCity",
        owner="KhaiMTC",
        floor=3
    )
    return resident
@router.post('/news/search-page')
async def news_search_page(request: news_dto.NewsSearchPageInput, db: Session = Depends(get_db)):
    # check = await check_auth(request.sid)
    # if check.get('data') > 0:
        res = await residential_repo.search_news_page(db,request.current_page,request.page_size)
        total = await residential_repo.total(db)
        # data = res.get('page_list_data')
        paginate_data = paginate(data=res, total=total, page_num=request.current_page, page_size=request.page_size)
        return CommonResponse.value(200, 'Success', paginate_data)
    # else:
    #     return CommonResponse.value(500, 'Error', None)


@router.post('/notification/search-page')
async def notification_search_page(param: common_dto.SearchPageInput,
                                   request: Request, db: Session = Depends(get_db)):
    try:
        _sid = request.headers.get('sid')
        check = await check_auth(_sid)
        if check.get('data') > 0:
            res = await residential_repo.search_notification_page(check.get('data'), param, db)
            data_page = {
                "page_list_data": res,
                "size": param.page_size,
                "total_pages": "",
                "total_items": "",
                "current_page": param.current_page if param.current_page > 0 else 0,
            }
            return CommonResponse.value(200, 'Success', data_page)
        else:
            return CommonResponse.value(500, 'Error', None)

    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)


@router.post('/banner/search-page')
async def banner_search_page(param: common_dto.SearchPageInput,
                             request: Request, db: Session = Depends(get_db)):
    try:
        _sid = request.headers.get('sid')
        check = await check_auth(_sid)
        if check.get('data') > 0:
            res = await residential_repo.search_banner_page(param, db)
            data_page = {
                "page_list_data": res,
                "size": param.page_size,
                "total_pages": "",
                "total_items": "",
                "current_page": param.current_page if param.current_page > 0 else 0,
            }
            return CommonResponse.value(200, 'Success', data_page)
        else:
            return CommonResponse.value(500, 'Error', None)

    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)



