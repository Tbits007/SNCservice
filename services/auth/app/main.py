from fastapi import FastAPI
from app.producer import get_producer

import asyncio
from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaConnectionError

KAFKA_BROKER = "kafka:9092"  # Адрес вашего брокера Kafka

async def wait_for_kafka():
    while True:
        try:
            # Пытаемся подключиться к Kafka
            producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BROKER)
            await producer.start()
            await producer.stop()
            print(f"Kafka is available at {KAFKA_BROKER}")
            break
        except KafkaConnectionError:
            print(f"Kafka is not available yet at {KAFKA_BROKER}. Retrying...")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(wait_for_kafka())

producer = get_producer()

from app.api import auth


app = FastAPI()


app.include_router(auth.router)


@app.on_event("startup")
async def startup_event():
    await producer.start()


@app.on_event("shutdown")
async def shutdown_event():
    await producer.stop()