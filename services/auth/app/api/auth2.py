from typing import Annotated
from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends, Response
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, models
from app.core.hash import get_password_hash
from app.schemas.user_schemas import CreateUserSchema, ReadUserSchema
from app.core.jwt import (
    create_token_pair,
    decode_access_token,
    add_refresh_token_cookie,
    JTI,
    EXP,
)

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/register", response_model=ReadUserSchema)
async def register(
    data: CreateUserSchema,
    db: AsyncSession = Depends(get_db),
):
    user = await models.User.find_by_email(db=db, email=data.email)
    if user:
        raise HTTPException(status_code=400, detail="Email has already registered")

    # hashing password
    user_data = data.model_dump()
    user_data["password"] = get_password_hash(user_data["password"])

    # save user to db
    user = models.User(**user_data)
    user.is_active = False
    await user.save(db=db)

    return user_schema


# @router.post("/login")
# async def login(
#     data: schemas.UserLogin,
#     response: Response,
#     db: AsyncSession = Depends(get_db),
# ):
#     user = await models.User.authenticate(
#         db=db, email=data.email, password=data.password
#     )

#     if not user:
#         raise BadRequestException(detail="Incorrect email or password")

#     if not user.is_active:
#         raise ForbiddenException()

#     user = schemas.User.from_orm(user)

#     token_pair = create_token_pair(user=user)

#     add_refresh_token_cookie(response=response, token=token_pair.refresh.token)

#     return {"token": token_pair.access.token}


# @router.post("/logout", response_model=schemas.SuccessResponseScheme)
# async def logout(
#     token: Annotated[str, Depends(oauth2_scheme)],
#     db: AsyncSession = Depends(get_db),
# ):
#     payload = await decode_access_token(token=token, db=db)
#     black_listed = models.BlackListToken(
#         id=payload[JTI], expire=datetime.utcfromtimestamp(payload[EXP])
#     )
#     await black_listed.save(db=db)

#     return {"msg": "Succesfully logout"}