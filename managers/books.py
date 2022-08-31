from db import db
from models import AudioBooksForApprovalModel, ReadingBooksForApprovalModel, DigitalBooksForApprovalModel, \
    ReadingBooksModel, StandardUserModel, DigitalBooksModel, AudioBooksModel, Status
from schemas.responce.books import ReadingBooksSchemaResponse, DigitalBooksSchemaResponse, AudioBooksSchemaResponse
from utils.validators import validate_existing_isbn


class BooksManager:
    @staticmethod
    def get():
        reading_books = ReadingBooksModel.query.all()
        digital_books = DigitalBooksModel.query.all()
        audio_books = AudioBooksModel.query.all()

        return ReadingBooksSchemaResponse().dump(reading_books, many=True), \
               DigitalBooksSchemaResponse().dump(digital_books, many=True), \
               AudioBooksSchemaResponse().dump(audio_books, many=True)


# Manager for reading books and reading books for approval tables
class ReadingBooksManager:
    # returns user's collection of reading books
    @staticmethod
    def get_books(user):
        books = ReadingBooksModel.query.join(StandardUserModel, ReadingBooksModel.users). \
            filter(StandardUserModel.id == user.id)
        return ReadingBooksSchemaResponse().dump(books, many=True)

    # creates
    @staticmethod
    def create(book_data):
        book = ReadingBooksForApprovalModel(**book_data)

        # check for the isbn in the tables. If ISBN exists in the DB raises BadRequest
        validate_existing_isbn(book_data["isbn"], ReadingBooksModel)
        validate_existing_isbn(book_data["isbn"], ReadingBooksForApprovalModel)

        db.session.add(book)
        return book

    # change book status in approval table from pending to approve and create a new book in official table
    @staticmethod
    def approve(book_id):
        ReadingBooksForApprovalModel.query.filter_by(id=book_id).update({"status": Status.approved})

        book = ReadingBooksForApprovalModel.query.filter_by(id=book_id).first()
        book_dict = dict((col, getattr(book, col)) for col in book.__table__.columns.keys())
        # TODO Refactor this :(
        book_dict.pop("id")
        book_dict.pop("status")
        app_book = ReadingBooksModel(**book_dict)
        db.session.add(app_book)
        return app_book

    @staticmethod
    def reject(book_id):
        ReadingBooksForApprovalModel.query.filter_by(id=book_id).update({"status": Status.rejected.name})
        return 204


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
