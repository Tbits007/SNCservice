from aiokafka import AIOKafkaProducer
from app.core.config import settings


class AIOAuthProducer:
    def __init__(self):
        self.__producer = AIOKafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        )
        self.__produce_topic = settings.PRODUCE_TOPIC

    async def start(self) -> None:
        if not self.__producer._closed:  # Проверяем, что продюсер ещё не запущен
            await self.__producer.start()

    async def stop(self) -> None:
        if not self.__producer._closed:  # Проверяем, что продюсер ещё не остановлен
            await self.__producer.stop()

    async def send(self, value: bytes) -> None:
        await self.__producer.send(
            topic=self.__produce_topic,
            value=value,
        )


def get_producer() -> AIOAuthProducer:
    return AIOAuthProducer()