import time
from sqlalchemy.orm import Session
from config import get_settings
import keygen
import models

import schemas


def create_db_url(db: Session, url: schemas.BaseURL) -> models.URL:
    key = keygen.create_random_key()
    expiry = int(time.time()) + (get_settings().time_limit * 3600)
    
    db_url = models.URL(
        original_url=url.original_url,
        key=key,
        expiry=expiry
        )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_if_key_exists(db: Session, url_key: str) -> models.URL:
   return db.query(models.URL).filter(models.URL.key == url_key).first()

def update_db_clicks(db: Session, db_url: schemas.URL) -> models.URL:
    db_url.visits += 1
    db.commit()
    db.refresh(db_url)
    return db_url

