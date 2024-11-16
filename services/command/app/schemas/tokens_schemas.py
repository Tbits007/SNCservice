import datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class TokenCreateSchema(BaseModel):
    user_id: UUID
    token: str
    expires_at: datetime.datetime


class TokenUpdateSchema(BaseModel):
    user_id: Optional[UUID] = None
    token: Optional[str] = None
    expires_at: Optional[datetime.datetime] = None
    
    
class TokenReadSchema(BaseModel):
    id: UUID
    user_id: UUID
    token: str
    expires_at: datetime.datetime

    class Config:
        from_attributes = True