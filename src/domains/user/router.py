from fastapi import APIRouter, Depends

from src.domains.user.request_schema import PatchUserRequestBodyDto, PostUserCreateRequestBodyDto
from src.domains.user.response_schema import (
    DeleteUserResponseDto,
    GetUserResponseDto,
    GetUsersResponseDto,
)
from src.domains.user.service import UserService

router = APIRouter(prefix="/users", tags=["users"])


def _get_service():
    return UserService()


@router.get("", response_model=GetUsersResponseDto)
def get_users(user_service: UserService = Depends(_get_service)):
    users = user_service.get_users()
    return GetUsersResponseDto(users=users)


@router.get("/{user_id}", response_model=GetUserResponseDto)
def get_user(user_id: int, user_service: UserService = Depends(_get_service)):
    user = user_service.get_user(user_id)
    return GetUserResponseDto.dto_parse(user)


@router.post("", response_model=GetUserResponseDto)
def create_user(
    body: PostUserCreateRequestBodyDto,
    user_service: UserService = Depends(_get_service),
):
    new_user = user_service.create_user(body.name)
    return GetUserResponseDto.dto_parse(new_user)


@router.patch("/{user_id}", response_model=GetUserResponseDto)
def patch_user(
    user_id: int,
    body: PatchUserRequestBodyDto,
    user_service: UserService = Depends(_get_service),
):
    updated_user = user_service.patch_user(user_id, body.name)
    return GetUserResponseDto.dto_parse(updated_user)


@router.delete("/{user_id}", response_model=DeleteUserResponseDto)
def delete_user(user_id: int, user_service: UserService = Depends(_get_service)):
    deleted_user, remain_count = user_service.delete_user(user_id)
    return DeleteUserResponseDto.dto_parse(deleted_user=deleted_user, remain_count=remain_count)
