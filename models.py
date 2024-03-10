from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    secret_key = Column(String, unique=True, index=True)
    original_url = Column(String, index=True)
    active = Column(Boolean, default=True)
    visits= Column(Integer, default=0)