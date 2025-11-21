from fastapi import APIRouter, Depends

from src.domains.user.schema_request import PatchUserRequestBodyDto, PostUserCreateRequestBodyDto
from src.domains.user.schema_response import (
    DeleteUserResponseDto,
    GetUserResponseDto,
    GetUsersResponseDto,
)
from src.domains.user.service import UserService

router = APIRouter(prefix="/users", tags=["users"])


def _get_service():
    return UserService()


@router.get("", response_model=GetUsersResponseDto)
async def get_users(user_service: UserService = Depends(_get_service)):
    users = await user_service.get_users()
    return GetUsersResponseDto(users=users)


@router.get("/{user_id}", response_model=GetUserResponseDto)
async def get_user(user_id: int, user_service: UserService = Depends(_get_service)):
    user = await user_service.get_user(user_id)
    return GetUserResponseDto.dto_parse(user)


@router.post("", response_model=GetUserResponseDto)
async def create_user(
    body: PostUserCreateRequestBodyDto,
    user_service: UserService = Depends(_get_service),
):
    new_user = await user_service.create_user(body.name)
    return GetUserResponseDto.dto_parse(new_user)


@router.patch("/{user_id}", response_model=GetUserResponseDto)
async def patch_user(
    user_id: int,
    body: PatchUserRequestBodyDto,
    user_service: UserService = Depends(_get_service),
):
    updated_user = await user_service.patch_user(user_id, body.name)
    return GetUserResponseDto.dto_parse(updated_user)


@router.delete("/{user_id}", response_model=DeleteUserResponseDto)
async def delete_user(user_id: int, user_service: UserService = Depends(_get_service)):
    deleted_user, remain_count = await user_service.delete_user(user_id)
    return DeleteUserResponseDto.dto_parse(deleted_user=deleted_user, remain_count=remain_count)
