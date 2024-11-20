import uuid
from typing import Optional
from pydantic import BaseModel


class BaseUser(BaseModel):
    service: str = "UserService" 

    class Config:
        json_schema_extra = {
            "example": {
                "email": "string",
                "hashed_password": "string",
                "is_active": True,
                "is_superuser": True
            }
        }    


class CreateUserSchema(BaseUser):
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool

    action: str = "create_user"


class UpdateUserSchema(BaseUser):
    email: Optional[str] = None
    hashed_password: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    
    action: str = "update_user"


class ReadUserSchema(BaseUser):
    id: uuid.UUID
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool

    action: str = "get_user_by_id"