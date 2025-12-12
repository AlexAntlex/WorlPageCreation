from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    name: str
    email: EmailStr
    bio: str
    avatar_url: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserCreate):
    name: str | None = None
    email: EmailStr | None = None
    bio: str | None = None
    avatar_url: str | None = None


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
