from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.subscriptions_repo import SubscriptionsRepository
from app.domain.subscriptions import Subscriptions
from app.schemas.subscriptions_schemas import SubscriptionCreateSchema


class SubscriptionService:
    def __init__(self, session: AsyncSession):
        self.subscription_repo = SubscriptionsRepository(session)  # Используйте ваш репозиторий


    async def get_all_subscriptions(self) -> list[Subscriptions]:
        # здесь можно добавить дополнительную логику
        return await self.subscription_repo.get_all()  # Получите всех пользователей через репозиторий


    async def get_subscription_by_id(self, subscription_id: UUID) -> Subscriptions | None:
        # здесь можно добавить дополнительную логику
        subscription = await self.subscription_repo.get_by_id(subscription_id)
        if subscription is None:
            raise HTTPException(status_code=500)
        return subscription
    

    async def create_subscription(self, data: SubscriptionCreateSchema) -> Subscriptions:
        subscription = Subscriptions(
            user_id=data.user_id,
            subscription_type=data.subscription_type,
            start_date=data.start_date,
            end_date=data.end_date,
        )
        return await self.subscription_repo.create(subscription)
    

    async def update_subscription(self, subscription_id: UUID, updated_data: dict) -> Subscriptions:
        await self.get_subscription_by_id(subscription_id)
        return await self.subscription_repo.update(subscription_id, updated_data)


    async def delete_subscription(self, subscription_id: UUID) -> None:
        await self.get_subscription_by_id(subscription_id)
        await self.subscription_repo.delete(subscription_id)
