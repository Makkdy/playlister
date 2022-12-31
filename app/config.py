# from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    db_keyspace: str
    db_client_secret: str
    db_client_id: str

    class Config:
        env_file = ".env"


settings = Settings()
# @lru_cache
# def get_settings():
#     return Settings
