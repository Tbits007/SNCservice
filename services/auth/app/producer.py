import brotli
from aiokafka import AIOKafkaProducer
from app.core.config import settings


async def compress(message: str) -> bytes:

    return brotli.compress(
        bytes(message, settings.file_encoding),
        quality=settings.file_compression_quality,
    )


def create_producer() -> AIOKafkaProducer:
    return AIOKafkaProducer(
        bootstrap_servers=settings.kafka_instance,
    )


producer_ = create_producer()