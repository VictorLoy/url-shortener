from fastapi import FastAPI
import validators
from error import raiseError
import schemas

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World , URL Shortener here"

@app.get("/url")
def create_url(url: schemas.BaseURL):
    if not validators.url(url.target_url):
        raiseError(statusCode=404, message="Your provided URL is not valid")
    return f"TODO: Create database entry for: {url.target_url}"



