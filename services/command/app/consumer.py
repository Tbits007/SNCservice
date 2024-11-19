import json
import brotli
from aiokafka import AIOKafkaConsumer

from app.core.config import settings
from app.core.database import async_session_maker
from typing import Callable
from app.services.users_service import UserService


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
            await process_task(value)


async def process_task(data: dict) -> None:
    # Получаем сервис по имени из data["service"]
    service_class = globals().get(data["service"])
    # Создаем экземпляр сервиса
    async with async_session_maker() as session:
        service = service_class(session)
        # Получаем действие
        action = data.get("action")
        # Получаем метод для выполнения действия
        action_method: Callable = getattr(service, action)
        # Выполняем действие
        result = await action_method(data)
        print(f"{type(result)} successfully created!")
