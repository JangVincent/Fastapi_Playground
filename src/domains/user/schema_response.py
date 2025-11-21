from pydantic import BaseModel

from src.core.dtos.dto_base_model import DTOBaseModel


class UserBaseDto(DTOBaseModel):
    id: int
    name: str


class GetUserResponseDto(UserBaseDto):
    pass


class GetUsersResponseDto(BaseModel):
    users: list[UserBaseDto]


class DeleteUserResponseDto(DTOBaseModel):
    deleted_user: UserBaseDto
    remain_count: int
