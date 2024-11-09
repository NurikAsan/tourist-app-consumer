from sqlalchemy import (
    Column, Integer, Float,
    String
)
from src.domain.models.base import Base


class Transfer(Base):
    __tablename__ = 'transfer'

    tour_id = Column(Integer)
    user_id = Column(Integer)
    sum = Column(Float)
    requisite = Column(String(256))
    adult = Column(Integer, nullable=True)
    children = Column(Integer, nullable=True)
