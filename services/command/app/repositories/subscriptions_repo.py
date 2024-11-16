from typing import Type
from app.domain.subscriptions import Subscriptions
from app.repositories.base_repo import BaseRepository


class SubscriptionsRepository(BaseRepository[Subscriptions]):
    model: Type[Subscriptions] = Subscriptions
