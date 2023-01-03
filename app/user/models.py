import uuid
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from pydantic import EmailStr
from . import hash
# from app.user.schemas import UserIn
from . import validator
from . import hash

# settings = get_settings()


class User(Model):
    __keyspace__ = "video_membership_app"
    email = columns.Text(primary_key=True)
    user_id = columns.UUID(primary_key=True, default=uuid.uuid1)
    password = columns.Text()

    def __repr__(self):
        return f"User(email={self.email}, user_id={self.user_id})"

    def __str__(self):
        return self.__repr__()

    def set_password(self, pw, commit=False):
        pw_hash = hash.generate_hash(pw)
        self.password = pw_hash
        if commit:
            self.save()
        return True

    def verify_password(self, pw):
        pw_hash = self.password
        verified, msg = hash.verify_password(pw_hash)
        return verified

    @staticmethod
    def createuser(user):
        q = User.objects.filter(email=user.email).all()
        if not q:
            valid, msg, email = validator._validate_email(user.email)
            if not valid:
                raise Exception("Invalid email:", {email})
            obj = User(email=user.email)
            obj.password = hash_password(user.password)
            obj.save()
        else:
            raise Exception(f"User with {user.email} already exist")
        return obj
