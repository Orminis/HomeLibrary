from datetime import datetime, timedelta

import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from werkzeug.exceptions import Unauthorized

from models import StandardUserModel


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.id, "role": user.role.name, "exp": datetime.utcnow() + timedelta(days=5), }
        return jwt.encode(payload, key=config("SECRET_KEY"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        if not token:
            raise Unauthorized("Missing token")
        try:
            payload = jwt.decode(token, key=config("SECRET_KEY"), algorithms=["HS256"])
            return [payload["sub"], payload["role"]]
        except ExpiredSignatureError:
            raise Unauthorized("Token expired")
        except InvalidTokenError:
            raise Unauthorized("Invalid token")


auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    try:
        user = AuthManager.decode_token(token)
        user_id, user_type = user[0], user[1]
        # return StandardUserModel.query.filter_by(id=user_id).first()
        return f"{user_type}.query.filter_by(id={user_id}).first()"
    except Exception:
        raise Unauthorized("Invalid or missing token")
