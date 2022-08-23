from db import db
from models import AudioBooksForApprovalModel, ReadingBooksForApprovalModel, DigitalBooksForApprovalModel


class ReadingBooksManager:
    @staticmethod
    def create(book_data):
        book = ReadingBooksForApprovalModel(**book_data)
        db.session.add(book)
        db.session.commit()
        return "Book added for approval.", 201


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


class AcceptBookManager:
    @staticmethod
    # TODO Update of accepted books
    def update(data):
        pass
