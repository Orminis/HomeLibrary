from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.users import UserManager
from schemas.request.auth import RegisterSchemaRequest, LoginSchemaRequest
from utils.decorators import validate_schema


class RegisterResource(Resource):
    @validate_schema(RegisterSchemaRequest)
    def post(self):
        data = request.get_json()
        token = UserManager.register(data)
        return {"token": token}, 201


class LoginResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = UserManager.login(data)
        return {"token": token}, 200


# TODO
class UpdateUserResource(Resource):
    @auth.login_required
    def put(self):
        data = request.get_json()
        pass