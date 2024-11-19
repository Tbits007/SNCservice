import json
import brotli
from aiokafka import AIOKafkaConsumer
from fastapi import FastAPI

from app.core.config import settings
from app.services.users_service import UserService
from app.core.database import async_session_maker


def create_application() -> FastAPI:
    """Create FastAPI application and set routes.

    Returns:
        FastAPI: The created FastAPI instance.
    """

    return FastAPI()


def create_consumer() -> AIOKafkaConsumer:

    return AIOKafkaConsumer(
        settings.kafka_topics,
        bootstrap_servers=settings.kafka_instance,
    )


app = create_application()
consumer = create_consumer()


async def decompress(file_bytes: bytes) -> dict:
    decompressed_str = str(
        brotli.decompress(file_bytes),
        settings.file_encoding,
    )
    return json.loads(decompressed_str)


async def consume():
    while True:
        async for msg in consumer:
            print(
                "consumed: ",
                f"topic: {msg.topic},",
                f"partition: {msg.partition},",
                f"offset: {msg.offset},",
                f"key: {msg.key},",
                f"value: {await decompress(msg.value)},",
                f"timestamp: {msg.timestamp}",
            )
            value = await decompress(msg.value)
            print("tyta -->", type(value), value)
            await process_task(value)


async def process_task(data: dict) -> None:
    async with async_session_maker() as session:
        user_service = UserService(session)
        user = await user_service.create_user(data)
        print("User created... ->")
        user_id = await user_service.get_user_by_id(user.id)
        print("Got a user_id... ->")
        print(user_id)

    
@app.on_event("startup")
async def startup_event():
    """Start up event for FastAPI application."""
    await consumer.start()
    await consume()


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event for FastAPI application."""
    await consumer.stop()
