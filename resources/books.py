from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.books import ReadingBooksManager, AudioBooksManager, DigitalBooksManager
from schemas.request.books import ReadingBookSchemaRequest, AudioBookSchemaRequest, DigitalBooksSchemaRequest
from utils.decorators import validate_schema


# Creating reading book resource
class ReadingBooksResource(Resource):
    @auth.login_required
    # @permission_required(UserRoles.user)
    @validate_schema(ReadingBookSchemaRequest)
    def post(self):
        data = request.get_json()
        book = ReadingBooksManager.create(data)
        return {"book": book}


# Creating digital book resource
class DigitalBooksResource(Resource):
    @auth.login_required
    @validate_schema(DigitalBooksSchemaRequest)
    def post(self):
        data = request.get_json()
        digital_book = DigitalBooksManager.create(data)
        return {"digital_book": digital_book}


# Creating audiobook resource
class AudioBooksResource(Resource):
    @auth.login_required
    @validate_schema(AudioBookSchemaRequest)
    def post(self):
        data = request.get_json()
        audio_book = AudioBooksManager.create(data)
        return {"audio_book": audio_book}
