from sqlalchemy.orm import Session

from app import models, schemas


def get_register_delivery(db: Session, register_delivery_id: int):
    return db.query(models.User).filter(models.RegisterDeliveryModel.id == register_delivery_id).first()


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