from src import database_fastapi
from src.schemas import fastapi_dto
from src.models import fastapi_models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from src.repository import user_fastapi_repo

router = APIRouter(
    prefix="/userfastapi",
    tags=['Users FastAPI']
)

get_db = database_fastapi.get_db


@router.post('/', response_model=fastapi_dto.ShowUser)
def create_user(request: fastapi_dto.User, db: Session = Depends(get_db)):
    return user_fastapi_repo.create(request, db)


@router.get('/{id}', response_model=fastapi_dto.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_fastapi_repo.show(id, db)
