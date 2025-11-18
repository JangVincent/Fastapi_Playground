from sqlalchemy import Column, Integer, String

from src.external.database.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
