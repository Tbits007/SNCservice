from fastapi import FastAPI
from app.consumer import consume, consumer_


def create_application() -> FastAPI:
    """Create FastAPI application and set routes."""
    return FastAPI()


app = create_application()


@app.on_event("startup")
async def startup_event():
    """Start up event for FastAPI application."""
    await consumer_.start()
    await consume()


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event for FastAPI application."""
    await consumer_.stop()
