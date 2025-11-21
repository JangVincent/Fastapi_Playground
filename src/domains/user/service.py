import logging
from typing import List, Tuple

from src.core.exception.exceptions import ConflictError, NotFoundError
from src.domains.user.response_schema import UserBaseDto
from src.external.database.unit_of_work import AsyncUnitOfWork
from src.external.database.uow_decorator import UoW

logger = logging.getLogger(__name__)


class UserService:
    uow: AsyncUnitOfWork  # 타입힌트만 (실제 할당 없음)

    @UoW
    async def get_users(self) -> List[UserBaseDto]:
        users = await self.uow.users.get_all_users()
        parsed_users = [UserBaseDto.dto_parse(user) for user in users]
        return parsed_users

    @UoW
    async def get_user(self, user_id: int) -> UserBaseDto:
        user = await self.uow.users.get_user_by_id(user_id)
        if not user:
            raise NotFoundError("User not found")
        return UserBaseDto.dto_parse(user)

    @UoW
    async def create_user(self, name: str) -> UserBaseDto:
        exist = await self.uow.users.get_user_by_name(name)
        if exist:
            raise ConflictError("User already exists")

        new_user = await self.uow.users.create_user(name)
        return UserBaseDto.dto_parse(new_user)

    @UoW
    async def patch_user(self, user_id: int, new_name: str) -> UserBaseDto:
        user = await self.uow.users.get_user_by_id(user_id)
        if not user:
            raise NotFoundError("User not found")

        duplicated_name_user = await self.uow.users.get_user_by_name(new_name)
        if duplicated_name_user and duplicated_name_user.id != user_id:
            raise Exception("Same name user already exists")

        patched_user = await self.uow.users.update_user(user, new_name)
        return UserBaseDto.dto_parse(patched_user)

    @UoW
    async def delete_user(self, user_id: int) -> Tuple[UserBaseDto, int]:
        user = await self.uow.users.get_user_by_id(user_id)
        if not user:
            raise NotFoundError("User not found")

        await self.uow.users.delete_user(user)
        remain_count = await self.uow.users.get_users_count()

        return UserBaseDto.dto_parse(user), remain_count
