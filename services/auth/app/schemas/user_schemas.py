from enum import Enum
import uuid
from typing import Optional
from pydantic import BaseModel, Field


class UserActionsEnum(str, Enum):
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"


class BaseUser(BaseModel):
    service: str = "UserService"
    action: UserActionsEnum | None = None


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


class UpdateUserSchema(BaseUser):
    email: Optional[str] = None
    hashed_password: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    

class ReadUserSchema(BaseUser):
    service: str = Field(default="UserService", exclude=True)
    action: UserActionsEnum | None = Field(default=None, exclude=True)

    id: uuid.UUID
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
