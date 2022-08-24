from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models.users import StandardUserModel
from models.association import *

class UserManager:
    @staticmethod
    def register(register_data):
        existing_mail = StandardUserModel.query.filter_by(email=register_data["email"]).first()
        existing_user = StandardUserModel.query.filter_by(username=register_data["username"]).first()
        if existing_mail or existing_user:
            raise BadRequest("Credentials already in use!")
        register_data["password"] = generate_password_hash(register_data["password"])
        user = StandardUserModel(**register_data)
        db.session.add(user)
        db.session.commit()
        return AuthManager.encode_token(user)

    @staticmethod
    def login(login_data):
        login_user = StandardUserModel.query.filter_by(email=login_data["email"]).first()
        if not login_user:
            raise BadRequest("No such User! Please register")
        if check_password_hash(login_user.password, login_data["password"]):
            return AuthManager.encode_token(login_user)
        raise BadRequest("Wrong credentials!")

    # login via (username or email) & password
    # if "email" in login_data:
    #     login_user = StandardUserModel.query.filter_by(email=login_data["email"]).first()
    # elif login_data[0] == "username":
    #     login_user = StandardUserModel.query.filter_by(username=login_data["username"]).first()
    # if not login_user:
    #     raise BadRequest("No such User! Please register")
    # if check_password_hash(login_user.password, login_data["password"]):
    #     return AuthManager.encode_token(login_user)
    # raise BadRequest("Wrong credentials!")

    @staticmethod
    def update(update_data):
        pass