from sqlalchemy.orm import Session

from app import models, schemas


def get_register_delivery(db: Session, register_delivery_id: int):
    return db.query(models.RegisterDeliveryModel).filter(
        models.RegisterDeliveryModel.id == register_delivery_id).first()


def get_register_deliveries(db: Session, skip: int = 0, limit: int = 100):
    register_delivery_models = db.query(models.RegisterDeliveryModel).offset(skip).limit(limit).all()
    total = db.query(models.RegisterDeliveryModel).count()
    return register_delivery_models, total


def create_register_delivery(db: Session, register_delivery: schemas.RegisterDeliveryCreate):
    db_register_delivery = models.RegisterDeliveryModel(**register_delivery.dict())
    db.add(db_register_delivery)
    db.commit()
    db.refresh(db_register_delivery)
    return db_register_delivery


def update_register_delivery(db: Session, register_delivery_id: int,
                             register_delivery_update: schemas.RegisterDeliveryUpdate):
    try:
        db_register_delivery = db.query(models.RegisterDeliveryModel).filter(
            models.RegisterDeliveryModel.id == register_delivery_id).first()

        for key, value in register_delivery_update.dict().items():
            db_register_delivery[key] = value

        db.commit()
        return db_register_delivery
    except Exception as ex:
        db.rollback()