from db import db
from models import ReadingBooksModel


class ReadingBooksManager:
    @staticmethod
    def create(book_data):
        book = ReadingBooksModel(**book_data)
        db.session.add(book)
        db.session.commit()
        return "Book added for approval", 201
