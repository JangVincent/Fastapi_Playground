from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from src.external.database.base import Base


class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_users_count(self):
        return self.session.query(UserModel).count()

    def get_all_users(self):
        return self.session.query(UserModel).all()

    def get_user_by_id(self, user_id: int):
        return self.session.query(UserModel).filter(UserModel.id == user_id).first()

    def get_user_by_name(self, name: str):
        return self.session.query(UserModel).filter(UserModel.name == name).first()

    def create_user(self, name: str):
        new_user = UserModel(name=name)
        self.session.add(new_user)
        self.session.flush()
        return new_user

    def update_user(self, user: UserModel, new_name: str):
        user.name = new_name
        self.session.add(user)
        self.session.flush()
        return user

    def delete_user(self, user: UserModel):
        self.session.delete(user)
        self.session.flush()
