import json
import brotli
from aiokafka import AIOKafkaConsumer
from app.core.config import settings
from app.core.database import async_session_maker
from typing import Callable
from app.services.users_service import UserService
from app.producer import compress, producer_
from app.schemas.users_schemas import UserReadSchema
from app.handler import handle_request


async def decompress(file_bytes: bytes) -> dict:
    decompressed_str = str(
        brotli.decompress(file_bytes),
        settings.file_encoding,
    )
    return json.loads(decompressed_str)


def create_consumer() -> AIOKafkaConsumer:

    return AIOKafkaConsumer(
        settings.kafka_topics,
        bootstrap_servers=settings.kafka_instance,
    )


consumer_ = create_consumer()


async def consume():
    while True:
        async for msg in consumer_:
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
            await handle_request(value)
