from fastapi import APIRouter, Path, Security, UploadFile, Form
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from starlette import status as http_status

from app.database import get_db
from app.repository.paginate_repo import paginate
from app.repository import residential_repo
from app.routers.userauth import check_auth
from app.schemas.user import User
from app.schemas.apartment import Apartment
from app.schemas.resident import Resident
from app.schemas.common import CommonResponse
from app.services import auth_service, utilities_service, complain_service
import app.schemas as Schemas

router = APIRouter(
    prefix="/residential",
    tags=['Residential API']
)


@router.get("/apartments")
async def get_apartments():
    try:
        aparments = []
        for i in range(1, 5):
            residents = []
            for j in range(1, 3):
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
        return CommonResponse.value(200, 'Success', apartment)
    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)


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
async def news_search_page(request: Schemas.NewsSearchPageInput, db: Session = Depends(get_db)):
    res = await residential_repo.search_news_page(db, request.current_page, request.page_size)
    total = await residential_repo.total(db)
    paginate_data = paginate(data=res, total=total, page_num=request.current_page, page_size=request.page_size)
    return CommonResponse.value(200, 'Success', paginate_data)


@router.post('/notification/search-page')
async def notification_search_page(param: Schemas.SearchPageInput,
                                   request: Request, db: Session = Depends(get_db)):
    try:
        _sid = request.headers.get('sid')
        check = await check_auth(_sid)
        if check.get('data') > 0:
            res = await residential_repo.search_notification_page(check.get('data'), param, db)
            total = await residential_repo.count_notifications(id=check.get('data'), db=db)
            paginate_data = paginate(data=res, total=total, page_num=param.current_page, page_size=param.page_size)
            return CommonResponse.value(200, 'Success', paginate_data)
        else:
            return CommonResponse.value(500, 'Error', None)

    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)


@router.put('/notification/read/{id}')
async def read_notification(id: int, request: Request, db: Session = Depends(get_db)):
    try:
        _sid = request.headers.get('sid')
        check = await check_auth(_sid)
        if check.get('data') > 0:
            await residential_repo.read_notification(id=id, db=db)
            return CommonResponse.value(200, 'Success', id)
        else:
            return CommonResponse.value(500, 'Error', None)

    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)


@router.get('/notification/count-unread-notifications')
async def total_unread_notifications(request: Request, db: Session = Depends(get_db)):
    try:
        _sid = request.headers.get('sid')
        check = await check_auth(_sid)
        if check.get('data') > 0:
            total = await residential_repo.count_unread_notifications(id=check.get('data'), db=db)
            return CommonResponse.value(200, 'Success', total)
        else:
            return CommonResponse.value(500, 'Error', None)

    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)


@router.post('/banner/search-page')
async def banner_search_page(param: Schemas.SearchPageInput,
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


@router.get(
    '/utilities',
    summary="List apartment utilities"
)
async def list_apartment_utilities(request: Schemas.SearchPageInput,
                                   user: User = Security(auth_service.auth_user),
                                   db: Session = Depends(get_db)):
    try:
        res = await utilities_service.get_list(db, request, user)
        return CommonResponse.value(200, 'Success', res)
    except Exception as e:
        return CommonResponse.value(500, e.args[0], None)


@router.post(
    '/complain',
    summary="Create residential complain"
)
async def create_claim(image: UploadFile,
                       name: str = Form(),
                       content: str = Form(),
                       blockhouse_id: int = Form(),
                       building_id: int = Form(),
                       user: User = Security(auth_service.auth_user),
                       db: Session = Depends(get_db)):
    try:
        data = dict(name=name,
                    content=content,
                    blockhouse_id=blockhouse_id,
                    building_id=building_id,
                    image=image)
        res = await complain_service.add(db, data, user)
        return CommonResponse.value(200, 'Success', res)
    except Exception as e:
        return CommonResponse.value(500, 'error', None)


@router.get(
    '/complain',
    summary="List residential complain"
)
async def get_claim(status: str,
                    current_page: int,
                    page_size: int,
                    user: User = Security(auth_service.auth_user),
                    db: Session = Depends(get_db)):
    try:
        data = dict(status=status,
                    current_page=current_page,
                    page_size=page_size)
        res = await complain_service.get_list(db, data, user)
        return CommonResponse.value(200, 'Success', res)
    except Exception as e:
        return CommonResponse.value(500, 'error', None)
