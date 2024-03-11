import secrets
import string

from config import get_settings
from sqlalchemy.orm import Session

import crud

def create_random_key(length: int = get_settings().key_length) -> str:
    chars = string.ascii_uppercase + string.ascii_lowercase +string.digits 
    return "".join(secrets.choice(chars) for _ in range(length))

def create_unique_random_key(db: Session) -> str:
    key = create_random_key()
    while crud.get_if_key_exists(db, key):
        key = create_random_key()
    return key