from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.users import UserManager
from models import UserRoles, StandardUserModel, users_reading_books_associations_table, ReadingBooksModel
from schemas.request.auth import RegisterSchemaRequest, LoginSchemaRequest, UpdateSchemaRequest
from schemas.responce.books import ReadingBooksSchemaResponse
from utils.decorators import validate_schema, permission_required


# Returns personal information for the user and his book collection
class PersonalUserResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.user)
    def get(self, user_id):
        token_user = auth.current_user()
        users_and_books = UserManager.get_user(token_user, user_id)
        info = [x for x in users_and_books if x]
        return info, 201


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


# Self update of current user # TODO Return
class UpdateUserResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.user)
    @validate_schema(UpdateSchemaRequest)
    def put(self, user_id):
        token_user = auth.current_user()
        current_user = StandardUserModel.query.filter_by(id=user_id).first()
        data = request.get_json()
        UserManager.update(data, token_user, user_id)
        return {current_user.username: "User credentials updated."}, 200


class DeleteUserResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.user)
    def delete(self, user_id):
        token_user = auth.current_user()
        user = UserManager.delete(token_user, user_id)
        return {user: "deleted!"}, 410


# TODO Nice return!!!
class AddReadingBookToCollectionResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.user)
    def put(self, book_id):
        book = UserManager.add_book_to_collection(book_id)
        return ReadingBooksSchemaResponse().dump(book)


class RemoveReadingBookFromCollectionResource(Resource):
    @auth.login_required
    @permission_required(UserRoles.user)
    def delete(self, book_id):
        book = ReadingBooksModel.query.filter_by(id=book_id).first()
        UserManager.remove_book_from_collection(book_id)
        return ReadingBooksSchemaResponse().dump(book)
