import json
from fastapi import APIRouter
from app.producer import compress, producer_
from app.schemas.message import CreateUserMessage


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/register")
async def register(data: CreateUserMessage) -> None:
    json_string = json.dumps(data.model_dump())
    await producer_.send_and_wait("auth", await compress(json_string))