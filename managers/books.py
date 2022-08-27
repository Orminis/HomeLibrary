from db import db
from models import AudioBooksForApprovalModel, ReadingBooksForApprovalModel, DigitalBooksForApprovalModel, \
    ReadingBooksModel


class ReadingBooksManager:
    @staticmethod
    def create(book_data):
        book = ReadingBooksForApprovalModel(**book_data)
        db.session.add(book)
        db.session.commit()
        return 201

    # @staticmethod
    # def update(book_data): # receives book Id and status
    #     book_to_update = ReadingBooksForApprovalModel.query.filter_by(id=book_data["id"]).first()
    #     if book_data["status"] == "approved":
    #         book_to_update.status = "approved"
    #         book = {k: v for k, v in book_to_update.items() if k != "status"}
    #         app_book = ReadingBooksModel(**book)
    #         db.session.add(app_book)
    #     elif book_data["status"] == "rejected":
    #         book_to_update.status = "rejected"
    #
    #     db.session.commit
    #
    #     return 201


class DigitalBooksManager:
    @staticmethod
    def create(dig_book_data):
        dig_book = DigitalBooksForApprovalModel(**dig_book_data)
        db.session.add(dig_book)
        db.session.commit()
        return "Digital book added for approval.", 201


class AudioBooksManager:
    @staticmethod
    def create(audio_data):
        audio_book = AudioBooksForApprovalModel(**audio_data)
        db.session.add(audio_book)
        db.session.commit()
        return "Audio book added for approval.", 201








        # book_data = {**book_data}
        # approved_data = ReadingBooksForApprovalModel(**book_data)
        # db.session.add(approved_data)
        # book = {}
        # for k, v in book_data:
        #     if not k == "status":
        #         book[k] = v
        # app_book = ReadingBooksModel(book)
        # db.session.add(app_book)
        # db.session.commit()