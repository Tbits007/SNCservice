import logging
import brotli
from aiokafka import AIOKafkaProducer
from fastapi import FastAPI, APIRouter, Query
from app.core.config import settings

log = logging.getLogger("uvicorn")

router = APIRouter(
    tags=["Auth"]
)

async def compress(message: str) -> bytes:

    return brotli.compress(
        bytes(message, settings.file_encoding),
        quality=settings.file_compression_quality,
    )


@router.post("/")
async def produce_message(message: str = Query(...)) -> dict: # <------------------- DICT УБЕРИ ЭЭЭ
    print(message)
    await producer.send_and_wait("auth", await compress(message))
    return {'1': "324"}

def create_application() -> FastAPI:
    """Create FastAPI application and set routes.

    Returns:
        FastAPI: The created FastAPI instance.
    """

    application = FastAPI()
    application.include_router(router)
    return application


def create_producer() -> AIOKafkaProducer:

    return AIOKafkaProducer(
        bootstrap_servers=settings.kafka_instance,
    )


app = create_application()
producer = create_producer()


@app.on_event("startup")
async def startup_event():
    """Start up event for FastAPI application."""
    log.info("Starting up...")
    await producer.start()


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event for FastAPI application."""

    log.info("Shutting down...")
    await producer.stop()
