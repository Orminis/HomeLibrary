from sqlalchemy import update
from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models.users import StandardUserModel, CheckerModel, AdminModel
from utils.validators import validate_existing_email, validate_existing_username


class UserManager:
    @staticmethod
    def register(register_data):
        validate_existing_email(register_data["email"])
        validate_existing_username(register_data["username"])
        register_data["password"] = generate_password_hash(register_data["password"])
        user = StandardUserModel(**register_data)
        db.session.add(user)
        db.session.commit()
        return AuthManager.encode_token(user)

    @staticmethod
    def login(login_data):
        # TODO make validator
        login_user = StandardUserModel.query.filter_by(email=login_data["email"]).first()
        if not login_user:
            login_user = CheckerModel.query.filter_by(email=login_data["email"]).first()
            if not login_user:
                login_user = AdminModel.query.filter_by(email=login_data["email"]).first()
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
    def update(user_id, data):
        upd_user = StandardUserModel.query.filter(StandardUserModel.id == user_id).first()
        for k, v in data.items():
            if k == "email":
                validate_existing_email(data["email"])
            if k == "username":
                validate_existing_username(data["username"])
            if k == "password":
                v = generate_password_hash(v)
            setattr(upd_user, k, v)
        db.session.commit()
        return upd_user
