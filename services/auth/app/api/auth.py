from fastapi import APIRouter, Query
from app.producer import compress, producer_

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/")
async def produce_message(message: str = Query(...)) -> None: 
    print(message)
    await producer_.send_and_wait("auth", await compress(message))