from pydantic import BaseModel

class BaseURL(BaseModel):
    original_url: str

class URL(BaseURL):
    active: bool
    visits: int

    class Config:
        orm_mode = True

class URLInfo(URL):
    url: str
    admin_url: str