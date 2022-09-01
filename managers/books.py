import os
import uuid

from common import TEMP_DIR
from db import db
from managers.auth import auth
from models import ReadingBooksModel, DigitalBooksModel, AudioBooksModel, ReadingBooksForApprovalModel, Status, \
    DigitalBooksForApprovalModel, AudioBooksForApprovalModel, UserRoles
from schemas.responce.books import ReadingBooksSchemaResponse, DigitalBooksSchemaResponse, AudioBooksSchemaResponse
from utils.base import decode_file
from utils.decorators import permission_required
from utils.validators import validate_existing_isbn, validate_status_is_pending


class BooksManager:
    @staticmethod
    def get_all():
        reading_books = ReadingBooksModel.query.all()
        digital_books = DigitalBooksModel.query.all()
        audio_books = AudioBooksModel.query.all()

        return ReadingBooksSchemaResponse().dump(reading_books, many=True), \
               DigitalBooksSchemaResponse().dump(digital_books, many=True), \
               AudioBooksSchemaResponse().dump(audio_books, many=True)


# Manager for reading books and reading books for approval tables
class ReadingBooksManager:
    # returns reading books server collection
    @staticmethod
    def get_books():
        reading_books = ReadingBooksModel.query.all()
        return ReadingBooksSchemaResponse().dump(reading_books, many=True)

    # creates a book and put it in approval table for check by checker or admin
    @staticmethod
    def create(book_data):
        # todo Upload photo to s3
        # convert base64 to file
        # save to the server
        # upload to s3
        # delete file from the server
        # data["photo_url"] = add the valie of s3 bucket url
        file_name = f"{str(uuid.uuid4())}.{book_data['extension']}"
        path = os.path.join(TEMP_DIR, file_name)

        decode_file(path, book_data["cover"])


        book = ReadingBooksForApprovalModel(**book_data)

        # check for the isbn in the tables. If ISBN exists in the DB raises BadRequest
        validate_existing_isbn(book_data["isbn"], ReadingBooksModel)
        validate_existing_isbn(book_data["isbn"], ReadingBooksForApprovalModel)

        db.session.add(book)
        db.session.flush()
        return book

    # change book status in approval table from pending to approve and create a new book in official table
    @staticmethod
    def approve(book_id):
        ReadingBooksForApprovalModel.query.filter_by(id=book_id).update({"status": Status.approved})
        book = ReadingBooksForApprovalModel.query.filter_by(id=book_id).first()
        validate_existing_isbn(book.isbn, ReadingBooksModel)

        book_dict = dict((col, getattr(book, col)) for col in book.__table__.columns.keys())
        book_dict.pop("id")
        book_dict.pop("status")

        app_book = ReadingBooksModel(**book_dict)
        db.session.add(app_book)
        return app_book

    # change book status in approval table from pending to reject
    @staticmethod
    def reject(book_id):
        book = ReadingBooksForApprovalModel.query.filter_by(id=book_id).first()
        validate_status_is_pending(book.status)
        ReadingBooksForApprovalModel.query.filter_by(id=book_id).update({"status": Status.rejected})
        return 204

    # method to delete book by admin
    @staticmethod
    def delete(book_id):
        del_book = db.session.get(ReadingBooksModel, book_id)
        db.session.delete(del_book)
        return "Book deleted!"


class DigitalBooksManager:
    @staticmethod
    def create(dig_book_data):
        dig_book = DigitalBooksForApprovalModel(**dig_book_data)
        db.session.add(dig_book)
        return "Digital book added for approval.", 201


class AudioBooksManager:
    @staticmethod
    def create(audio_data):
        audio_book = AudioBooksForApprovalModel(**audio_data)
        db.session.add(audio_book)
        return "Audio book added for approval.", 201
