from fastapi import APIRouter, Depends

from src.domains.user.schema import (
    GetUserResponseDto,
    GetUsersResponseDto,
    PatchUserRequestBodyDto,
    PostUserCreateRequestBodyDto,
)
from src.domains.user.service import UserService

router = APIRouter(prefix="/users", tags=["users"])


def _get_service():
    return UserService()


@router.get("", response_model=GetUsersResponseDto)
def get_users(user_service: UserService = Depends(_get_service)):
    users = user_service.get_users()
    return {"users": users}


@router.get("/{user_id}", response_model=GetUserResponseDto)
def get_user(user_id: int, user_service: UserService = Depends(_get_service)):
    user = user_service.get_user(user_id)
    return user


@router.post("", response_model=GetUserResponseDto)
def create_user(
    body: PostUserCreateRequestBodyDto,
    user_service: UserService = Depends(_get_service),
):
    new_user = user_service.create_user(body.name)
    return new_user


@router.patch("/{user_id}", response_model=GetUserResponseDto)
def patch_user(
    user_id: int,
    body: PatchUserRequestBodyDto,
    user_service: UserService = Depends(_get_service),
):
    updated_user = user_service.patch_user(user_id, body.name)
    return updated_user


@router.delete("/{user_id}")
def delete_user(user_id: int, user_service: UserService = Depends(_get_service)):
    user_service.delete_user(user_id)
    return {"message": "User #" + str(user_id) + " deleted successfully."}
