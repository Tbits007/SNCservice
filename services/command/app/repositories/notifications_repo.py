from typing import Type
from app.domain.notifications import Notifications
from app.repositories.base_repo import BaseRepository


class NotificationsRepository(BaseRepository[Notifications]):
    model: Type[Notifications] = Notifications
