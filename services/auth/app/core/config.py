from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    KAFKA_HOST: str
    KAFKA_PORT: str
    kafka_instance = f"{KAFKA_PORT}:{KAFKA_PORT}"
    file_encoding: str = "utf-8"
    file_compression_quality: int = 1

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()