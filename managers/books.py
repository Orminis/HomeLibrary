import os
import uuid

from common import TEMP_DIR
from db import db
from models import ReadingBooksModel, DigitalBooksModel, AudioBooksModel, ReadingBooksForApprovalModel, Status, \
    DigitalBooksForApprovalModel, AudioBooksForApprovalModel, UserRoles
from schemas.responce.books import ReadingBooksSchemaResponse, DigitalBooksSchemaResponse, AudioBooksSchemaResponse
from services.s3 import S3Service
from utils.base import decode_file
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
        extension = book_data.pop("extension")
        cover_photo = book_data.pop("cover_photo_url")
        file_name = f"{str(uuid.uuid4())}.{extension}"
        path = os.path.join(TEMP_DIR, file_name)
        decode_file(path, cover_photo)
        s3 = S3Service()
        cover_photo_url = s3.upload_cover(path, file_name)

        book_data["cover_photo_url"] = cover_photo_url
        book = ReadingBooksForApprovalModel(**book_data)
        os.remove(path)

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
