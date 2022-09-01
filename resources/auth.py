from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.users import UserManager
from models import UserRoles
from schemas.request.auth import RegisterSchemaRequest, LoginSchemaRequest
from utils.decorators import validate_schema, permission_required


# Registering new user
class RegisterUserResource(Resource):
    @validate_schema(RegisterSchemaRequest)
    def post(self):
        data = request.get_json()
        token = UserManager.register(data)
        return {"token": token}, 201


# login for all roles
class LoginUserResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = UserManager.login(data)
        return {"token": token}, 200


# Deleting user (only he can do it)
class DeleteUserResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.user)
    def delete(self, user_id):
        token_user = auth.current_user()
        user = UserManager.delete(token_user, user_id)
        return {user: "deleted!"}, 202


# Creation of checker (only by admin)
class CreateCheckerResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.admin)
    def post(self):
        data = request.get_json()
        checker = UserManager.register_checker(data)
        return {checker: "created"}, 200


# Creation of admin (only by other admin)
class CreateAdminResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.admin)
    def post(self):
        data = request.get_json()
        admin = UserManager.register_admin(data)
        return {admin: "created"}, 200