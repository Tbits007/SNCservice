import logging

import brotli
from aiokafka import AIOKafkaConsumer
from fastapi import FastAPI

from app.core.config import settings

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    """Create FastAPI application and set routes.

    Returns:
        FastAPI: The created FastAPI instance.
    """

    return FastAPI()


def create_consumer() -> AIOKafkaConsumer:

    return AIOKafkaConsumer(
        settings.KAFKA_TOPICS,
        bootstrap_servers=settings.kafka_instance,
    )


app = create_application()
consumer = create_consumer()


async def decompress(file_bytes: bytes) -> str:
    return str(
        brotli.decompress(file_bytes),
        settings.file_encoding,
    )


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


@app.on_event("startup")
async def startup_event():
    """Start up event for FastAPI application."""

    log.info("Starting up...")
    await consumer.start()
    await consume()


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event for FastAPI application."""

    log.info("Shutting down...")
    await consumer.stop()
