from pydantic import BaseModel, EmailStr, SecretStr, validator


class UserSignUp(BaseModel):
    email: EmailStr
    password: SecretStr
    confirm_password: SecretStr

    # @validator()
    # def password_validator():
    #     if password != confirm_password:
    #         raise
