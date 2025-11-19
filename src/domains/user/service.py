from sqlalchemy.orm import Session

from src.entities.user_model import UserRepository


def _get_user_repository(session: Session) -> UserRepository:
    return UserRepository(session)


class UserService:
    def __init__(self, session: Session):
        self.session = session
        self.repository = _get_user_repository(session)

    def get_users(self):
        print("Get All Users")
        users = self.repository.get_all_users()
        return users

    def get_user(self, user_id: int):
        print("Get User by ID:", user_id)
        return self.repository.get_user_by_id(user_id)

    def create_user(self, name: str):
        print("Create a new user!", name)
        try:
            exist_user = self.repository.get_user_by_name(name)
            if exist_user:
                raise Exception("User with the same name already exists.")
            new_user = self.repository.create_user(name)

            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

        self.session.refresh(new_user)
        return new_user

    def patch_user(self, user_id: int, new_name: str):
        print("Patch User:", user_id, new_name)
        try:
            user = self.get_user(user_id)
            if not user:
                raise Exception("User not found.")

            exist_user = self.repository.get_user_by_name(new_name)
            if exist_user and exist_user.id != user_id:
                raise Exception("User with the same name already exists.")

            updated_user = self.repository.update_user(user, new_name)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

        self.session.refresh(updated_user)
        return updated_user

    def delete_user(self, user_id: int):
        print("Delete User:", user_id)
        try:
            user = self.get_user(user_id)
            if not user:
                raise Exception("User not found.")

            self.repository.delete_user(user)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

        return True
