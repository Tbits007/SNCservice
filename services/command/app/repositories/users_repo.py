from typing import Type
from app.domain.users import Users
from app.repositories.base_repo import BaseRepository
from typing import Generic, Type, TypeVar
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class UsersRepository(BaseRepository[Users]):
    model: Type[Users] = Users


    async def get_by_email(self, email: str) -> Users | None:
        """
        Получить запись по ID.
        """
        query = select(self.model).filter(self.model.email == email)
        result = await self.session.execute(query)

        return result.scalar_one_or_none() # <app.domain.users.Users object at 0x0000018CBC3CDD00> | None
