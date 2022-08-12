from flask import request
from flask_restful import Resource

from managers.users import UserManager


class RegisterResource(Resource):
    # TODO Validation of data
    def post(self):
        data = request.get_json()
        token = UserManager.register(data)
        return {"token": token}, 201
