import validators
from database import SessionLocal
from error import raiseError
import models
import schemas
import secrets
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return "Hello World , URL Shortener here"

@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.BaseURL, db: Session = Depends(get_db)):
    if not validators.url(url.original_url):
        raiseError(statusCode=404, message="Invalid URL")
    
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))
    db_url = models.URL(
        original_url=url.original_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key

    return db_url



