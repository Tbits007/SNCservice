import datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class SubscriptionCreateSchema(BaseModel):
    user_id: UUID
    subscription_type: str
    start_date: datetime.datetime
    end_date: datetime.datetime


class SubscriptionUpdateSchema(BaseModel):
    user_id: Optional[UUID] = None
    subscription_type: Optional[str] = None
    start_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None
    
    
class SubscriptionReadSchema(BaseModel):
    id: UUID
    user_id: UUID
    subscription_type: str
    start_date: datetime.datetime
    end_date: datetime.datetime

    class Config:
        from_attributes = True