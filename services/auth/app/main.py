from fastapi import FastAPI
from services.auth.app.api import auth

app = FastAPI()

app.include_router(auth.router)
