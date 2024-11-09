from pydantic.v1 import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=True,
        extra='ignore',
    )
    POSTGRES_USER: Optional[str]
    POSTGRES_PASSWORD: Optional[str]
    POSTGRES_HOST: Optional[str]
    POSTGRES_PORT: Optional[str]
    POSTGRES_DB: Optional[str]
