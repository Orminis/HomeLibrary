from werkzeug.security import generate_password_hash

from db import db
from managers.auth import AuthManager
from models.users import StandardUserModel


class UserManager:
    @staticmethod
    def register(register_data):
        register_data["password"] = generate_password_hash(register_data["password"])
        user = StandardUserModel(**register_data)
        db.session.add(user)
        db.session.commit()
        return AuthManager.encode_token(user)
