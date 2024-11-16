from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.notifications_repo import NotificationsRepository
from app.domain.notifications import Notifications
from app.schemas.notifications_schemas import NotificationCreateSchema, NotificationUpdateSchema, NotificationReadSchema


class NotificationService:
    def __init__(self, session: AsyncSession):
        self.notification_repo = NotificationsRepository(session)  # Используйте ваш репозиторий


    async def get_all_notifications(self) -> list[NotificationReadSchema]:
        # Получите все уведомления через репозиторий
        return await self.notification_repo.get_all()


    async def get_notification_by_id(self, notification_id: UUID) -> NotificationReadSchema:
        # Получите уведомление по ID
        notification = await self.notification_repo.get_by_id(notification_id)
        if notification is None:
            raise HTTPException(status_code=500)
        return notification


    async def create_notification(self, data: NotificationCreateSchema) -> NotificationReadSchema:
        # Создайте новое уведомление
        notification = Notifications(
            user_id=data.user_id,
            message=data.message,
        )
        return await self.notification_repo.create(notification)


    async def update_notification(self, notification_id: UUID, updated_data: NotificationUpdateSchema) -> NotificationReadSchema:
        # Обновите уведомление
        await self.get_notification_by_id(notification_id)  # Проверка, что объект существует
        return await self.notification_repo.update(notification_id, updated_data)


    async def delete_notification(self, notification_id: UUID) -> None:
        # Удалите уведомление
        await self.get_notification_by_id(notification_id)  # Проверка, что объект существует
        await self.notification_repo.delete(notification_id)
