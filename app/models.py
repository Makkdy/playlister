import uuid
from .config import settings
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns

# settings = get_settings()
print(settings.db_client_id)


class User(Model):
    __keyspace__ = "video_membership_app"
    email = columns.Text(primary_key=True)
    user_id = columns.UUID(primary_key=True, default=uuid.uuid1)
    password = columns.Text()

    def __repr__(self):
        return f"User(email={self.email}, user_id={self.user_id})"

    def __str__(self):
        return self.__repr__()
