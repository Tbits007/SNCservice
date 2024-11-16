from typing import Type
from app.domain.tokens import Tokens
from app.repositories.base_repo import BaseRepository


class TokensRepository(BaseRepository[Tokens]):
    model: Type[Tokens] = Tokens
from typing import Type
from app.domain.tokens import Tokens
from app.repositories.base_repo import BaseRepository


class TokensRepository(BaseRepository[Tokens]):
    model: Type[Tokens] = Tokens