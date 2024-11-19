from pydantic import BaseModel


class CreateUserMessage(BaseModel):
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    
    service: str = "UserService" 
    action: str = "create_user"

    class Config:
        json_schema_extra = {
            "example": {
                "email": "string",
                "hashed_password": "string",
                "is_active": True,
                "is_superuser": True
            }
        }