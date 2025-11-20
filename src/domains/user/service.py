from src.external.database.unit_of_work import UnitOfWork
from src.external.database.uow_decorator import UoW


class UserService:
    uow: UnitOfWork  # 타입힌트만 (실제 할당 없음)

    @UoW
    def get_users(self):
        return self.uow.users.get_all_users()

    @UoW
    def get_user(self, user_id: int):
        user = self.uow.users.get_user_by_id(user_id)
        if not user:
            raise Exception("User not found.")
        return user

    @UoW
    def create_user(self, name: str):
        exist = self.uow.users.get_user_by_name(name)
        if exist:
            raise Exception("User exists")

        return self.uow.users.create_user(name)

    @UoW
    def patch_user(self, user_id: int, new_name: str):
        user = self.uow.users.get_user_by_id(user_id)
        if not user:
            raise Exception("User not found.")

        conflict = self.uow.users.get_user_by_name(new_name)
        if conflict and conflict.id != user_id:
            raise Exception("User with same name exists")

        return self.uow.users.update_user(user, new_name)

    @UoW
    def delete_user(self, user_id: int):
        user = self.uow.users.get_user_by_id(user_id)
        if not user:
            raise Exception("User not found.")

        self.uow.users.delete_user(user)
        return True
