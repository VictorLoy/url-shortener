import time
from fastapi.responses import RedirectResponse
import validators
from config import get_settings
import crud
from database import SessionLocal
from error import raiseError
import models
import schemas
from fastapi import Depends, FastAPI, Request
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
    
    db_url = crud.create_db_url(db=db, url=url)
    db_url.url = db_url.key


    return db_url

@app.get("/{url_key}")
def forward_to_original_url(
        url_key: str,
        request: Request,
        db: Session = Depends(get_db)
    ):
    db_url = crud.get_if_key_exists(db, url_key)
    if db_url:
        print(int(time.time()), db_url.expiry , int(time.time()) > db_url.expiry)
        if db_url.active and int(time.time()) < db_url.expiry:
            crud.update_db_clicks(db, db_url)
            return RedirectResponse(db_url.original_url)
        else:
            raiseError(statusCode=410 , message=f" URL {request.url} not active or expired")
    else:
        raiseError(statusCode=404,message=f" URL {request.url} not found")

@app.post("/admin/{url_key}", response_model=schemas.AdminInfo)
def forward_to_original_url(
        url_key: str,
        request: Request,
        db: Session = Depends(get_db)
    ):
    db_url = crud.get_if_key_exists(db, url_key)
    if db_url:
        db_url.url = db_url.key
        return db_url
    else:
        raiseError(statusCode=404,message=f" URL {request.url} not found")



