import json
from fastapi import APIRouter, Depends, FastAPI
from services.auth.app.producer import AIOAuthProducer, get_producer
from services.auth.app.schemas.message import CreateUserMessage


router = APIRouter(
    prefix="/auth",
)


@router.post("/register")
async def send(
    message: CreateUserMessage,
    producer: AIOAuthProducer = Depends(get_producer)
    ) -> None:
    
    message_to_produce = json.dumps(message.model_dump()).encode(encoding="utf-8")
    await producer.send(value=message_to_produce)