import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    kafka_host: str = os.getenv("KAFKA_HOST")
    kafka_port: str = os.getenv("KAFKA_PORT")
    kafka_instance: str = f"{kafka_host}:{kafka_port}"
    file_encoding: str = "utf-8"
    file_compression_quality: int = 1
    
    
settings = Settings()

