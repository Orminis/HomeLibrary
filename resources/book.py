from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.books import ReadingBooksManager
from models import UserRoles
from schemas.request.books import ReadingBookSchemaRequest
from utils.decorators import permission_required, validate_schema


# Creating book resource
class ReadingBooksResource(Resource):
    @auth.login_required
    # @permission_required(UserRoles.user)
    @validate_schema(ReadingBookSchemaRequest)
    def post(self):
        data = request.get_json()
        book = ReadingBooksManager.create(data)
        return {"book": book}
