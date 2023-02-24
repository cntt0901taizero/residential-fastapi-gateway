from fastapi import APIRouter, Query, Depends, Body, Path
from sqlalchemy.orm import Session
from typing import List
from app.repository.register_delivery_repo import get_register_deliveries, create_register_delivery, get_register_delivery, update_register_delivery
from app import schemas
from app.database import get_db

router = APIRouter(prefix='register-delivery', )

@router.get(response_model=schemas.RegisterDeliveryListRespone)
def get_register_deliveries(
    page_size: int = Query(..., title="Page size", min=10),
    offset: int = Query(..., title='Offset', min=0),
    db: Session = Depends(get_db),
):
    db_models, total = get_register_deliveries(page_size=page_size, offset=offset, db=db)
    return schemas.RegisterDeliveryListRespone(data=db_models, total=total)

@router.post(response_model=schemas.RegisterDelivery)
def get_register_deliveries(
    body: schemas.RegisterDeliveryCreate = Body(..., title="Register Delivery Create"),
    db: Session = Depends(get_db)
):
    response = create_register_delivery(db=db, register_delivery=body)
    return response

@router.get('/{id}', respone_model=schemas.RegisterDelivery)
def get_register_delivery_details(
    id: int = Path(..., title="Register delivery id", min=0),
    db: Session = Depends(get_db),
):
    response = get_register_delivery(db=db, register_delivery_id=id)
    return response


@router.put('/{id}', respone_model=schemas.RegisterDeliveryUpdate)
def get_register_delivery_details(
    id: int = Path(..., title="Register delivery id", min=0),
    body: schemas.RegisterDeliveryUpdate = Body(..., title="Register Delivery Update"),
    db: Session = Depends(get_db),
):
    response = update_register_delivery(db=db, register_delivery_id=id, register_delivery_update=body)

    return response