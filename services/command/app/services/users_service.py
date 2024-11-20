from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.users_repo import UsersRepository
from app.domain.users import Users


class UserService:
    def __init__(self, session: AsyncSession):
        self.user_repo = UsersRepository(session)  # Используйте ваш репозиторий


    async def get_all_users(self) -> list[Users]:
        # здесь можно добавить дополнительную логику
        return await self.user_repo.get_all()  # Получите всех пользователей через репозиторий


    async def get_user_by_id(self, user_id: UUID) -> Users | None:
        # здесь можно добавить дополнительную логику
        user = await self.user_repo.get_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=500)
        return user
    

    async def get_user_by_email(self, email: str) -> Users | None:
        # здесь можно добавить дополнительную логику
        user = await self.user_repo.get_by_email(email)
        if user is None:
            raise HTTPException(status_code=500)
        return user
    
    
    async def create_user(self, data: dict) -> Users:
        user = Users(
            email=data["email"],
            hashed_password=data["hashed_password"],
            is_active=data["is_active"],
            is_superuser=data["is_superuser"],
        )
        return await self.user_repo.create(user)
    

    async def update_user(self, user_id: UUID, updated_data: dict) -> Users:
        await self.get_user_by_id(user_id)
        return await self.user_repo.update(user_id, updated_data)


    async def delete_user(self, user_id: UUID) -> None:
        await self.get_user_by_id(user_id)
        await self.user_repo.delete(user_id)

        