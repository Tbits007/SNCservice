import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_USER: str = os.getenv("POSTGRES_USER")
    DB_PASS: str = os.getenv("POSTGRES_PASSWORD")
    DB_NAME: str = os.getenv("POSTGRES_DB")
    DB_HOST: str = os.getenv("POSTGRES_HOST")
    DB_PORT: int = os.getenv("POSTGRES_PORT")

    kafka_host: str = os.getenv("KAFKA_HOST")
    kafka_port: str = os.getenv("KAFKA_PORT")
    kafka_topics: str = os.getenv("KAFKA_TOPICS")
    kafka_instance: str = f"{kafka_host}:{kafka_port}"
    file_encoding: str = "utf-8"
    file_compression_quality: int = 1
    
    #model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    @property
    def DATABASE_URL(self):
      return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
