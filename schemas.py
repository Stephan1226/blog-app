from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# User 스키마
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Post 스키마
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    author_id: int

class PostUpdate(PostBase):
    pass

class Post(PostBase):
    id: int
    author_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    author: Optional[User] = None

    class Config:
        from_attributes = True 