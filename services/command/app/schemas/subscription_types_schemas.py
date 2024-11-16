from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class SubscriptionTypeCreateSchema(BaseModel):
    name: str
    description: str
    price: float


class SubscriptionTypeUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    
    
class SubscriptionTypeReadSchema(BaseModel):
    id: UUID
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True