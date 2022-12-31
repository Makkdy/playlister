from .config import get_settings()

settings = get_settings()

print(settings.db_keyspace)
