from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def generate_hash(password):
    ph = PasswordHasher()
    return ph.hash(password)


def verify_password(user_password, correct_password):
    ph = PasswordHasher()
    verified = False
    msg = ""
    try:
        verified = ph.verify(user_password, correct_password)
    except VerifyMismatchError:
        varified = False
        msg = "Invalid Password"
    except Exception as e:
        verified = False
        msg = f"Say welcome to error: {e}"
    return verified, msg


# password = "Hello World!"

# print(hash_password(password))
