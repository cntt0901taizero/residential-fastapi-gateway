from sqlalchemy.orm import Session

from app import models


def get_block_house(db: Session, blockhouse_id: int):
    return db.query(models.Blockhouse).filter(models.Blockhouse.id == blockhouse_id).first()