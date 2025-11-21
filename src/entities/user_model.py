from typing import List

from sqlalchemy import Column, Integer, String, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.external.database.base import Base


class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_users_count(self) -> int:
        result = await self.session.execute(select(func.count()).select_from(UserModel))
        return result.scalar()

    async def get_all_users(self) -> List[UserModel]:
        return (await self.session.execute(select(UserModel))).scalars().all()

    async def get_user_by_id(self, user_id: int) -> UserModel | None:
        return (
            await self.session.execute(select(UserModel).filter(UserModel.id == user_id))
        ).scalar_one_or_none()

    async def get_user_by_name(self, name: str) -> UserModel | None:
        return (
            await self.session.execute(select(UserModel).filter(UserModel.name == name))
        ).scalar_one_or_none()

    async def create_user(self, name: str) -> UserModel:
        user = UserModel(name=name)
        self.session.add(user)
        await self.session.flush()
        return user

    async def update_user(self, user: UserModel, new_name: str) -> UserModel:
        user.name = new_name
        self.session.add(user)
        await self.session.flush()
        return user

    async def delete_user(self, user: UserModel) -> None:
        await self.session.delete(user)
        await self.session.flush()
        await self.session.flush()
