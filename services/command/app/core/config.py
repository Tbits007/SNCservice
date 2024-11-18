from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str 
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    KAFKA_HOST: str 
    KAFKA_PORT: str 
    KAFKA_TOPICS: str
    kafka_instance = f"{KAFKA_HOST}:{KAFKA_PORT}"
    file_encoding: str = "utf-8"
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
