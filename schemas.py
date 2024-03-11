from pydantic import BaseModel

class BaseURL(BaseModel):
    original_url: str

class URL(BaseURL):
    active: bool

    class Config:
        orm_mode = True

class URLInfo(URL):
    url: str
    expiry: float

class AdminInfo(URL):
    url: str
    expiry: float
    visits: int
    created: float
    expiry: float


