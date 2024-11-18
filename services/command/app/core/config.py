import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # DB_HOST: str 
    # DB_PORT: int
    # DB_USER: str
    # DB_PASS: str
    # DB_NAME: str

    kafka_host: str = os.getenv("KAFKA_HOST")
    kafka_port: str = os.getenv("KAFKA_PORT")
    kafka_topics: str = os.getenv("KAFKA_TOPICS")
    kafka_instance: str = f"{kafka_host}:{kafka_port}"
    file_encoding: str = "utf-8"
    
    #model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    #@property
    #def DATABASE_URL(self):
    #   return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
