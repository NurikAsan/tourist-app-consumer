from sqlalchemy import (
    DateTime,
    MetaData,
    func,
    Column,
    Integer,
)
from sqlalchemy.orm import declarative_base


DeclarativeBase = declarative_base(metadata=MetaData(schema='core'))


class Base(DeclarativeBase):
    __abstract__ = True
    __table_args__ = {'schema': 'core'}

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, index=True, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
