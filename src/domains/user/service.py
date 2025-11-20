from typing import List

from src.domains.user.response_schema import GetUserResponseDto, UserBaseDto
from src.entities.user_model import User
from src.external.database.unit_of_work import UnitOfWork
from src.external.database.uow_decorator import UoW


class UserService:
    uow: UnitOfWork  # 타입힌트만 (실제 할당 없음)

    @UoW
    def get_users(self) -> List[UserBaseDto]:
        users = self.uow.users.get_all_users()
        parsed_users = [UserBaseDto.dto_parse(user) for user in users]
        return parsed_users

    @UoW
    def get_user(self, user_id: int):
        user = self.uow.users.get_user_by_id(user_id)
        if not user:
            raise Exception("User not found.")
        return UserBaseDto.dto_parse(user)

    @UoW
    def create_user(self, name: str):
        exist = self.uow.users.get_user_by_name(name)
        if exist:
            raise Exception("User exists")

        return UserBaseDto.dto_parse(self.uow.users.create_user(name))

    @UoW
    def patch_user(self, user_id: int, new_name: str):
        user = self.uow.users.get_user_by_id(user_id)
        if not user:
            raise Exception("User not found.")

        duplicated_name_user = self.uow.users.get_user_by_name(new_name)
        if duplicated_name_user and duplicated_name_user.id != user_id:
            raise Exception("User with same name exists")

        return UserBaseDto.dto_parse(self.uow.users.update_user(user, new_name))

    @UoW
    def delete_user(self, user_id: int):
        user = self.uow.users.get_user_by_id(user_id)
        if not user:
            raise Exception("User not found.")

        self.uow.users.delete_user(user)
        remain_count = self.uow.users.get_users_count()

        return UserBaseDto.dto_parse(user), remain_count
