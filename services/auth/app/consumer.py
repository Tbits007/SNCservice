import json
import brotli
from aiokafka import AIOKafkaConsumer

from app.core.config import settings


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
            return value