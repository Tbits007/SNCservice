import json
from fastapi import APIRouter
from app.schemas.message import CreateUserMessage
from app.main import producer


router = APIRouter(
    prefix="/auth",
)


@router.post("/register")
async def user_register(
    message: CreateUserMessage,
    ) -> None:
    
    message_to_produce = json.dumps(message.model_dump()).encode(encoding="utf-8")
    await producer.send(value=message_to_produce)

#uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
