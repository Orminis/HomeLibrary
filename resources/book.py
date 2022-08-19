from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.books import ReadingBooksManager, AudioBooksManager
from schemas.request.books import ReadingBookSchemaRequest, AudioBookSchemaRequest
from utils.decorators import validate_schema


# Creating book resource
class ReadingBooksResource(Resource):
    @auth.login_required
    # @permission_required(UserRoles.user)
    @validate_schema(ReadingBookSchemaRequest)
    def post(self):
        data = request.get_json()
        book = ReadingBooksManager.create(data)
        return {"book": book}


class AudioBooksResource(Resource):
    @auth.login_required
    @validate_schema(AudioBookSchemaRequest)
    def post(self):
        data = request.get_json()
        audio_book = AudioBooksManager.create(data)
        return {"audio_book": audio_book}
