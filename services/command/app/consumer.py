import asyncio
import json
from aiokafka import AIOKafkaConsumer
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.users_service import UserService
from app.core.database import get_session
from app.schemas.users_schemas import UserCreateSchema


class AuthConsumer:
    def __init__(self, bootstrap_servers: str, topic: str, group_id: str):
        self._consumer = AIOKafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
        )

    async def start(self) -> None:
        """Старт консьюмера."""
        await self._consumer.start()

    async def stop(self) -> None:
        """Остановка консьюмера."""
        if self._consumer:
            await self._consumer.stop()

    async def consume(self, session: AsyncSession) -> None:
        """Чтение сообщений из Kafka."""
        while True:
            try:
                async for msg in self._consumer:
                    event = json.loads(msg.value.decode("utf-8"))
                    print(f"Received event from auth: {event}")
                    # Здесь можно вызвать обработчик события
                    await self.process_event(event, session)
            except Exception as e:
                print(f"Error consuming messages: {e}")
                await asyncio.sleep(5)

    async def process_event(self, event: dict, session: AsyncSession) -> None:
        """Обработка события (метод-заглушка)."""
        print(f"Processing event: {event}")
        # Реализуйте логику обработки события
        user_service = UserService(session)
        print("2!!")
        new_user = await user_service.create_user(event)
        print("HELLO, BEBRA", new_user)

# cd services/command
# uvicorn app.main:app --reload --host 0.0.0.0 --port 8002