from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.users import UserManager
from models import UserRoles, ReadingBooksModel, StandardUserModel
from schemas.request.auth import UpdateSchemaRequest
from schemas.responce.books import ReadingBooksSchemaResponse
from utils.decorators import permission_required, validate_schema


# Returns personal information for the user and his book collection
class PersonalUserResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.user)
    def get(self, user_id):
        token_user = auth.current_user()
        users_and_books = UserManager.get_user(token_user, user_id)
        info = [x for x in users_and_books if x]
        return info, 200


# Self update of current user
class UpdateUserResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.user)
    @validate_schema(UpdateSchemaRequest)
    def put(self, user_id):
        token_user = auth.current_user()
        current_user = StandardUserModel.query.filter_by(id=user_id).first()
        data = request.get_json()
        UserManager.update(data, token_user, user_id)
        return {current_user.username: "User credentials updated."}, 202


# Returns user's reading book collection
class UserReadingBooksResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.user)
    def get(self, user_id):
        token_user = auth.current_user()
        books = UserManager.get_reading_books(token_user)
        return ReadingBooksSchemaResponse().dump(books, many=True), 200


# Add a book to user's reading book collection
class AddReadingBookToCollectionResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.user)
    def put(self, book_id):
        book = UserManager.add_book_to_collection(book_id)
        return ReadingBooksSchemaResponse().dump(book), 201


# Remove a book from user's reading book collection
class RemoveReadingBookFromCollectionResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.user)
    def delete(self, book_id):
        book = ReadingBooksModel.query.filter_by(id=book_id).first()
        UserManager.remove_book_from_collection(book_id)
        return ReadingBooksSchemaResponse().dump(book), 202
