import datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class NotificationCreateSchema(BaseModel):
    user_id: UUID
    message: str


class NotificationUpdateSchema(BaseModel):
    user_id: Optional[UUID] = None
    message: Optional[str] = None

    
class NotificationReadSchema(BaseModel):
    id: UUID
    user_id: UUID
    message: str
    created_at: datetime.datetime

    class Config:
        from_attributes = True
