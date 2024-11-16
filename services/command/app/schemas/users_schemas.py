from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class UserCreateSchema(BaseModel):
    email: str
    hashed_password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


class UserUpdateSchema(BaseModel):
    email: Optional[str] = None
    hashed_password: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    
    
class UserReadSchema(BaseModel):
    id: UUID
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool

    class Config:
        from_attributes = True