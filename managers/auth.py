from datetime import datetime, timedelta

import jwt
from decouple import config
from jwt import ExpiredSignatureError, InvalidTokenError
from werkzeug.exceptions import Unauthorized
from flask_httpauth import HTTPTokenAuth

class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=5)}
        return jwt.encode(payload, key=config("SECRET_KEY"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        if not token:
            raise Unauthorized("Missing token")
        try:
            payload = jwt.decode(token, key=config("JWT_SECRET"), algorithms=["HS256"])
            return payload["sub"]
        except ExpiredSignatureError:
            raise Unauthorized("Token expired")
        except InvalidTokenError:
            raise Unauthorized("Invalid token")

    auth = HTTPTokenAuth(scheme='Bearer')

    @staticmethod
    @auth.verify_token
    def verify_token(token):
        try:
            user_id, type_user = AuthManager.decode_token(token)
            return eval(f"{type_user}.query.filter_by(id={user_id}).first()")
        except Exception as ex:
            raise Unauthorized("Invalid or missing token")