from typing import Union

from fastapi import Header, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.repository import building_house_repo
from app.schemas.apartment import House


async def get_house_info(
        hid: str = Header(default=None),
        db: Session = Depends(get_db)
):
    house = await building_house_repo.get_house_info(db, hid)
    return House.from_orm(house)
