from db import db

from models.enum import Covers, Status


class BooksModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author_name = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    isbn = db.Column(db.Integer, nullable=False)


class ReadingBooksModel(BooksModel):
    __tablename__ = "reading_books"

    original_language = db.Column(db.String(20), nullable=True)
    publish_language = db.Column(db.String(20), nullable=False)
    edition = db.Column(db.Integer, nullable=False)
    paper_format_cover = db.Column(db.Enum(Covers), nullable=True)
    # relation between standard users and reading books bidirectional
    users = db.relationship("StandardUserModel",
                            secondary="UsersReadingBooksAssociations",
                            back_populates="reading_books")


class DigitalBooksModel(BooksModel):
    __tablename__ = "digital_books"

    original_language = db.Column(db.String(20), nullable=True)
    publish_language = db.Column(db.String(20), nullable=False)
    edition = db.Column(db.Integer, nullable=False)
    # relation between standard users and reading books bidirectional
    users = db.relationship("StandardUserModel",
                            secondary="UsersDigitalBooksAssociations",
                            back_populates="digital_books")


class AudioBooksModel(BooksModel):
    __tablename__ = "audio_books"

    reader_name = db.Column(db.String(100), nullable=False)
    # relation between standard users and reading books bidirectional
    users = db.relationship("StandardUserModel",
                            secondary="UsersAudioBooksAssociations",
                            back_populates="audio_books")


class ReadingBooksForApprovalModel(BooksModel):
    __tablename__ = "reading_books_for_approval"

    original_language = db.Column(db.String(20), nullable=True)
    publish_language = db.Column(db.String(20), nullable=False)
    edition = db.Column(db.Integer, nullable=False)
    paper_format_cover = db.Column(db.Enum(Covers), nullable=True)
    status = db.Column(db.Enum(Status), default=Status.pending, nullable=False)


class DigitalBooksForApprovalModel(BooksModel):
    __tablename__ = "digital_books_for_approval"

    original_language = db.Column(db.String(20), nullable=True)
    publish_language = db.Column(db.String(20), nullable=False)
    edition = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum(Status), default=Status.pending, nullable=False)


class AudioBooksForApprovalModel(BooksModel):
    __tablename__ = "audio_books_for_approval"

    reader_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Enum(Status), default=Status.pending, nullable=False)
