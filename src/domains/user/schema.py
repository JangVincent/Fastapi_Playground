from pydantic import BaseModel


class UserBase(BaseModel):
  id: int

class PostUserCreateRequestBodyDto(UserBase):
  name: str

class GetUserResponseDto(UserBase):
  pass

class GetUsersResponseDto(BaseModel):
  users: list[UserBase]
