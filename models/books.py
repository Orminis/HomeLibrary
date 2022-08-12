from db import db

from models.enum import Covers, Status


class BookModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    author_first_name = db.Column(db.String(35), nullable=False)
    author_last_name = db.Column(db.String(35), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(Status), default=Status.pending, nullable=False)
    comments = db.Column(db.Text, nullable=True)


class ReadingBooksModel(BookModel):
    __tablename__ = "reading_books"

    original_language = db.Column(db.String(20), nullable=True)
    publish_language = db.Column(db.String(20), nullable=False)
    edition = db.Column(db.Integer, nullable=False)
    paper_format_cover = db.Column(db.Enum(Covers), nullable=False)
    digital_format = db.Column(db.String(20), nullable=True)


class AudioBookModel(BookModel):
    __tablename__ = "audio_books"

    reader_name = db.Column(db.String(100), nullable=False)