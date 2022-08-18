from flask import request
from flask_restful import Resource

from db import db
from managers.auth import auth
from managers.books import ReadingBooksManager
from models import UserRoles
from utils.decorators import permission_required


# Creating book resource
class ReadingBooksResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.user)
    def post(self):
        data = request.get_json()
        ReadingBooksManager.create(data)
        return 200
