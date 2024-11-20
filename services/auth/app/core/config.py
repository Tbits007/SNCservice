import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    kafka_host: str = os.getenv("KAFKA_HOST")
    kafka_port: str = os.getenv("KAFKA_PORT")
    kafka_instance: str = f"{kafka_host}:{kafka_port}"
    file_encoding: str = "utf-8"
    file_compression_quality: int = 1

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "sraGbRmjYQXmYdnrgPk!OFE35UP6n/QqeoED=iu/bUXBFSSPwnsuprP6T45Qsbwywu2khUka!6IIleY",
    )
    if not SECRET_KEY:
        SECRET_KEY = os.urandom(32)

    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRES_MINUTES = 30
    REFRESH_TOKEN_EXPIRES_MINUTES = 15 * 24 * 60  # 15 days

    
settings = Settings()

