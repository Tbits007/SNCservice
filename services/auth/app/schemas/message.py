from pydantic import BaseModel


class CreateUserMessage(BaseModel):
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    