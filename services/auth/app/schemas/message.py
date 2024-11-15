from uuid import UUID
from pydantic import BaseModel, EmailStr


class CreateUserMessage(BaseModel):
    id: UUID
    email: EmailStr
    hashed_password: str
    is_active: bool
    is_superuser: bool
    