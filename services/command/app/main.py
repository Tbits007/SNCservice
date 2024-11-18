# Пример интеграции с FastAPI
import asyncio
from fastapi import FastAPI
from app.core.database import async_session_maker
from app.consumer import AuthConsumer

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

app = FastAPI()

# Создаём экземпляр класса AuthConsumer
consumer = AuthConsumer(
    bootstrap_servers="kafka:9092",
    topic="auth",
    group_id="command_group",
)


@app.on_event("startup")
async def startup_event():
    """Событие старта приложения."""
    await consumer.start()

    async def consume_task():
        # Создаём сессию и передаём её в consumer
        async with async_session_maker() as session:
            await consumer.consume(session)

    asyncio.create_task(consume_task())


@app.on_event("shutdown")
async def shutdown_event():
    """Событие остановки приложения."""
    await consumer.stop()