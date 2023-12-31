from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class House(Base):
    __tablename__ = "houses"

    id = Column(String(10), primary_key=True, nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    location = Column(String(128), nullable=False)
    region = Column(String(64), nullable=False)
    type = Column(String(32), nullable=False)
    price = Column(String(16), nullable=False)
    bedrooms = Column(String(32), nullable=False)
    agent = Column(String(64), nullable=False)
    description = Column(String(512), nullable=False)
    sold = Column(String(4), nullable=False)
    sold_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now)

    def __repr__(self):
        return f"House( {self.id} , {self.location})"
