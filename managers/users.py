from werkzeug.exceptions import BadRequest, Forbidden
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager, auth
from models import ReadingBooksModel, DigitalBooksModel, AudioBooksModel
from models.users import StandardUserModel, CheckerModel, AdminModel
from schemas.responce.books import ReadingBooksSchemaResponse, DigitalBooksSchemaResponse, AudioBooksSchemaResponse
from schemas.responce.user import UserSchemaResponse
from utils.validators import validate_existing_email, validate_existing_username, validate_login_user, \
    validate_user_id_vs_token_id


class UserManager:
    @staticmethod
    def get_user(token_user, user_id):
        # If token id is different from given id raises Forbidden
        validate_user_id_vs_token_id(token_user, user_id)
        current_user = StandardUserModel.query.filter_by(id=token_user.id).first()
        books = ReadingBooksModel.query.join(StandardUserModel, ReadingBooksModel.users). \
            filter(StandardUserModel.id == token_user.id)
        digital_books = DigitalBooksModel.query.join(StandardUserModel, DigitalBooksModel.users). \
            filter(StandardUserModel.id == token_user.id)
        audio_books = AudioBooksModel.query.join(StandardUserModel, AudioBooksModel.users). \
            filter(StandardUserModel.id == token_user.id)
        return UserSchemaResponse().dump(current_user), ReadingBooksSchemaResponse().dump(books, many=True), \
               DigitalBooksSchemaResponse().dump(digital_books, many=True), \
               AudioBooksSchemaResponse().dump(audio_books, many=True)

    @staticmethod
    def register(register_data):
        validate_existing_email(register_data["email"])
        validate_existing_username(register_data["username"])
        register_data["password"] = generate_password_hash(register_data["password"])
        user = StandardUserModel(**register_data)
        db.session.add(user)
        return AuthManager.encode_token(user)

    @staticmethod
    def login(login_data):
        # validate login user via email
        login_user = validate_login_user(login_data)
        if not login_user:
            raise BadRequest("No such User! Please register")
        if check_password_hash(login_user.password, login_data["password"]):
            return AuthManager.encode_token(login_user)
        raise BadRequest("Wrong credentials!")

    # Update user credentials
    @staticmethod
    def update(data, token_user, user_id):
        # If token id is different from given id raises Forbidden
        validate_user_id_vs_token_id(token_user, user_id)
        upd_user = StandardUserModel.query.filter(StandardUserModel.id == user_id).first()
        for credentials, values in data.items():
            if credentials == "email":
                validate_existing_email(data["email"])
            if credentials == "username":
                validate_existing_username(data["username"])
            if credentials == "password":
                values = generate_password_hash(values)
            setattr(upd_user, credentials, values)
        return ...

    # method to delete user account by user
    @staticmethod
    def delete(token_user, user_id):
        # If token id is different from given id raises Forbidden
        validate_user_id_vs_token_id(token_user, user_id)

        del_user = db.session.get(StandardUserModel, user_id)
        db.session.delete(del_user)
        return "User deleted!"

    # Add book to user's collection
    @staticmethod
    def add_book_to_collection(user_id):
        current_user = auth.current_user()
        users_reading_books_associations_table