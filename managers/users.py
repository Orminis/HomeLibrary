from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

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

    @staticmethod
    def login(login_data):
        # login via (username or email) & password
        login_set = {"username", "email"}
        command = list(login_data.keys())[0]
        if command in login_set:
            login_user = StandardUserModel.query.filter_by(username=login_data[command]).first()
        if not login_user:
            raise BadRequest("No such User! Please register")
        if check_password_hash(login_user.password, login_data["password"]):
            return AuthManager.encode_token(login_user)
        raise BadRequest("Wrong credentials!")
