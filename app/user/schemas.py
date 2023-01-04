from .. import db
from pydantic import BaseModel, EmailStr, SecretStr, validator
from .models import User
from cassandra.cqlengine.management import sync_table

db.get_session()
sync_table(User)


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: SecretStr


class UserSignupSchema(BaseModel):
    email: EmailStr
    password: SecretStr
    password_confirm: SecretStr

    @validator("email")
    def available_email(cls, v, values, **kwargs):
        q = User.objects.filter(email=v)
        if q:
            raise ValueError(f"Email not available")
        else:
            return v

    @validator("password_confirm")
    def password_checking(cls, v, values, **kwargs):
        # alternative use, password --> values["password"]
        password = values["password"]
        if password != v:
            raise ValueError(f"Password do not match")
        else:
            return v
