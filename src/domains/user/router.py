
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.domains.user.schema import (GetUserResponseDto, GetUsersResponseDto,
                                     PostUserCreateRequestBodyDto)
from src.domains.user.service import UserService
from src.external.database.database import get_db

router = APIRouter(prefix ="/users", tags=["users"])

def _get_user_service(db: Session = Depends(get_db)):
    return UserService(db)

@router.get('', response_model=GetUsersResponseDto)
def get_users(user_service : UserService = Depends(_get_user_service)):
  users = user_service.get_users();
  return {"users": users}


@router.get("/{user_id}", response_model=GetUserResponseDto)
def get_user(user_id: int, user_service: UserService = Depends(_get_user_service)):
  user = user_service.get_user(user_id);
  return user

@router.post("", response_model=GetUserResponseDto)
def create_user(body : PostUserCreateRequestBodyDto, user_service: UserService = Depends(_get_user_service)):
  new_user = user_service.create_user(body.name)
  return new_user
