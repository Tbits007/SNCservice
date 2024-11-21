import json
import brotli
from aiokafka import AIOKafkaConsumer

from app.core.config import settings
from app.core.database import async_session_maker
from typing import Callable
from app.services.users_service import UserService
from app.producer import compress, producer_
from app.schemas.users_schemas import UserReadSchema
from sqlalchemy.inspection import inspect


def model_to_dict(model):
    return {str(column.key): str(getattr(model, column.key)) for column in inspect(model).mapper.column_attrs}


async def handle_request(data: dict) -> None:
    # Получаем сервис по имени из data["service"]
    service_class = globals().get(data["service"])
    # Создаем экземпляр сервиса
    async with async_session_maker() as session:
        service = service_class(session)
        # Получаем действие
        action = data.get("action")
        # Получаем метод для выполнения действия
        action_method: Callable = getattr(service, action)
        # Выполняем действие
        result = []
        try:
            result = await action_method(data)
        except Exception as e:
            print(e)
            data = [{"msg": "ERROR!"}]
            json_string = json.dumps(data)
            await producer_.send_and_wait("command_service", await compress(json_string))
        else:
            print("SDDDDDDDDDDDFSDDSF1111111", result)
            data = [model_to_dict(item) for item in result]
            json_string = json.dumps(data)
            await producer_.send_and_wait("command_service", await compress(json_string))