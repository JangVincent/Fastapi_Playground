from sqlalchemy import Column, Integer, String

from src.external.database.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class UserRepository:
    from sqlalchemy.orm import Session

    def __init__(self, session: Session):
        self.session = session

    def get_all_users(self):
        return self.session.query(User).all()

    def get_user_by_id(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).first()

    def get_user_by_name(self, name: str):
        return self.session.query(User).filter(User.name == name).first()

    def create_user(self, name: str):
        new_user = User(name=name)
        self.session.add(new_user)
        return new_user

    def update_user(self, user: User, new_name: str):
        user.name = new_name
        self.session.add(user)
        return user

    def delete_user(self, user: User):
        self.session.delete(user)
