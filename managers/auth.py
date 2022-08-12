from datetime import datetime, timedelta
import jwt
from decouple import config


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=5)}
        return jwt.encode(payload, key=config("SECRET_KEY"), algorith="HS256")
