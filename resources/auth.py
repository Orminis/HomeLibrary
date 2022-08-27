from flask import request
from flask_restful import Resource
from werkzeug.exceptions import Forbidden

from managers.auth import auth
from managers.users import UserManager
from models import UserRoles, StandardUserModel
from schemas.request.auth import RegisterSchemaRequest, LoginSchemaRequest, UpdateSchemaRequest
from utils.decorators import validate_schema, permission_required


class RegisterResource(Resource):
    @validate_schema(RegisterSchemaRequest)
    def post(self):
        data = request.get_json()
        token = UserManager.register(data)
        return {"token": token}, 201


# TODO to be used by any role
class LoginResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = UserManager.login(data)
        return {"token": token}, 200


# Self update of current user
class UpdateUserResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.user, UserRoles.admin)
    @validate_schema(UpdateSchemaRequest)
    def put(self, user_id):
        current_user = StandardUserModel.query.filter_by(id=user_id).first()
        if not current_user.id == user_id:
            raise Forbidden("Forbidden!")
        data = request.get_json()
        UserManager.update(user_id, data)
        return {current_user.username: "changed with new credentials"}, 200
