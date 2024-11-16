from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.tokens_repo import TokensRepository
from app.domain.tokens import Tokens
from app.schemas.tokens_schemas import TokenCreateSchema


class TokenService:
    def __init__(self, session: AsyncSession):
        self.token_repo = TokensRepository(session)  # Используйте ваш репозиторий


    async def get_all_tokens(self) -> list[Tokens]:
        # здесь можно добавить дополнительную логику
        return await self.token_repo.get_all()  # Получите всех пользователей через репозиторий


    async def get_token_by_id(self, token_id: UUID) -> Tokens | None:
        # здесь можно добавить дополнительную логику
        token = await self.token_repo.get_by_id(token_id)
        if token is None:
            raise HTTPException(status_code=500)
        return token
    

    async def create_token(self, data: TokenCreateSchema) -> Tokens:
        token = Tokens(
            user_id=data.user_id,
            token=data.token,
            expires_at=data.expires_at,
        )
        return await self.token_repo.create(token)
    

    async def update_token(self, token_id: UUID, updated_data: dict) -> Tokens:
        await self.get_token_by_id(token_id)
        return await self.token_repo.update(token_id, updated_data)


    async def delete_token(self, token_id: UUID) -> None:
        await self.get_token_by_id(token_id)
        await self.token_repo.delete(token_id)

        