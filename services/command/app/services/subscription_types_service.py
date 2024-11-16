from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.subscription_types_repo import SubscriptionTypesRepository
from app.domain.subscription_types import SubscriptionTypes
from app.schemas.subscription_types_schemas import SubscriptionTypeCreateSchema


class SubscriptionTypeService:
    def __init__(self, session: AsyncSession):
        self.subscription_type_repo = SubscriptionTypesRepository(session)  # Используйте ваш репозиторий


    async def get_all_subscription_types(self) -> list[SubscriptionTypes]:
        # Здесь можно добавить дополнительную логику
        return await self.subscription_type_repo.get_all()  # Получите все типы подписок через репозиторий


    async def get_subscription_type_by_id(self, subscription_type_id: UUID) -> SubscriptionTypes | None:
        # Здесь можно добавить дополнительную логику
        subscription_type = await self.subscription_type_repo.get_by_id(subscription_type_id)
        if subscription_type is None:
            raise HTTPException(status_code=500)
        return subscription_type
    

    async def create_subscription_type(self, data: SubscriptionTypeCreateSchema) -> SubscriptionTypes:
        subscription_type = SubscriptionTypes(
            name=data.name,
            description=data.description,
            price=data.price,
        )
        return await self.subscription_type_repo.create(subscription_type)
    

    async def update_subscription_type(self, subscription_type_id: UUID, updated_data: dict) -> SubscriptionTypes:
        await self.get_subscription_type_by_id(subscription_type_id)  # Проверка, что объект существует
        return await self.subscription_type_repo.update(subscription_type_id, updated_data)


    async def delete_subscription_type(self, subscription_type_id: UUID) -> None:
        await self.get_subscription_type_by_id(subscription_type_id)  # Проверка, что объект существует
        await self.subscription_type_repo.delete(subscription_type_id)
