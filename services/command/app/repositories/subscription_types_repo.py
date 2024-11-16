from typing import Type
from app.domain.subscription_types import SubscriptionTypes
from app.repositories.base_repo import BaseRepository


class SubscriptionTypesRepository(BaseRepository[SubscriptionTypes]):
    model: Type[SubscriptionTypes] = SubscriptionTypes
