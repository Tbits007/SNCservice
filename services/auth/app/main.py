from fastapi import FastAPI
from app.api import auth
from app.producer import producer_


def create_application() -> FastAPI:
    """Create FastAPI application and set routes.

    Returns:
        FastAPI: The created FastAPI instance.
    """
    application = FastAPI()
    application.include_router(auth.router)
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    """Start up event for FastAPI application."""
    await producer_.start()


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event for FastAPI application."""
    await producer_.stop()
