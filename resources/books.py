from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.books import (
    ReadingBooksManager,
    AudioBooksManager,
    DigitalBooksManager,
    BooksManager,
)
from models import UserRoles
from schemas.request.books import (
    ReadingBookSchemaRequest,
    AudioBookSchemaRequest,
    DigitalBooksSchemaRequest,
)
from schemas.responce.books import ReadingBooksSchemaResponse
from utils.decorators import validate_schema, permission_required


class BooksResource(Resource):
    @auth.login_required
    def get(self):
        books = BooksManager.get_all()
        return books, 200


class ReadingBooksResource(Resource):
    # Returns reading book collection
    @auth.login_required
    def get(self):
        books = ReadingBooksManager.get_books()
        return books, 200

    # Creating reading book resource
    @auth.login_required
    @validate_schema(ReadingBookSchemaRequest)
    def post(self):
        data = request.get_json()
        book = ReadingBooksManager.create(data)
        return ReadingBooksSchemaResponse().dump(book), 201


# TODO To update book information
#     @auth.login_required
#     @permission_required(UserRoles.checker, UserRoles.admin)
#     def put(self):
#         data = request.get_json()
#         book = ReadingBooksManager.update(data)
#         return book


class DeleteReadingBooksResource(Resource):
    # Delete a reading book
    @auth.login_required
    @permission_required(UserRoles.admin)
    def delete(self, book_id):
        book = ReadingBooksManager.delete(book_id)
        return {book: "deleted!"}, 200


# Creating digital book resource
class DigitalBooksResource(Resource):
    @auth.login_required
    @validate_schema(DigitalBooksSchemaRequest)
    def post(self):
        data = request.get_json()
        digital_book = DigitalBooksManager.create(data)
        return {"digital_book": digital_book}, 201


# Creating audiobook resource
class AudioBooksResource(Resource):
    @auth.login_required
    @validate_schema(AudioBookSchemaRequest)
    def post(self):
        data = request.get_json()
        audio_book = AudioBooksManager.create(data)
        return {"audio_book": audio_book}, 201


class ApproveReadingBookResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.checker, UserRoles.admin)
    def put(self, id):
        app_book = ReadingBooksManager.approve(id)
        return ReadingBooksSchemaResponse().dump(app_book), 201


class RejectReadingBookResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.checker, UserRoles.admin)
    def put(self, id):
        ReadingBooksManager.reject(id)
        return 202
