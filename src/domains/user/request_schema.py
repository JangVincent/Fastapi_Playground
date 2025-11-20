from pydantic import BaseModel


class PostUserCreateRequestBodyDto(BaseModel):
    name: str


class PatchUserRequestBodyDto(BaseModel):
    name: str
