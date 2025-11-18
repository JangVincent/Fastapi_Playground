from pydantic import BaseModel


class UserBase(BaseModel):
  id: int
  name: str

class PostUserCreateRequestBodyDto(BaseModel):
  name: str

class GetUserResponseDto(UserBase):
  pass

class GetUsersResponseDto(BaseModel):
  users: list[UserBase]
