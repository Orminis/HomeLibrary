from db import db
from models.enum import Covers, Status

users_reading_books_associations_table = db.Table("users_reading_books_associations", db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("standard_user.id")),
    db.Column("reading_book_id", db.Integer, db.ForeignKey("reading_books.id")))


users_digital_books_associations_table = db.Table("users_digital_books_associations", db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("standard_user.id")),
    db.Column("digital_book_id", db.Integer, db.ForeignKey("digital_books.id")))


users_audio_books_associations_table = db.Table("users_audio_books_associations", db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("standard_user.id")),
    db.Column("audio_book_id", db.Integer, db.ForeignKey("audio_books.id")))


class BooksModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author_name = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    isbn = db.Column(db.BigInteger, nullable=False, unique=True)


class ReadingBooksModel(BooksModel):
    __tablename__ = "reading_books"

    original_language = db.Column(db.String(20), nullable=True)
    publish_language = db.Column(db.String(20), nullable=False)
    edition = db.Column(db.Integer, nullable=False)
    paper_format_cover = db.Column(db.Enum(Covers), nullable=True)
    # relation between standard users and reading books bidirectional
    users = db.relationship("StandardUserModel",
                            secondary=users_reading_books_associations_table,
                            back_populates="reading_books")


class DigitalBooksModel(BooksModel):
    __tablename__ = "digital_books"

    original_language = db.Column(db.String(20), nullable=True)
    publish_language = db.Column(db.String(20), nullable=False)
    edition = db.Column(db.Integer, nullable=False)
    # relation between standard users and reading books bidirectional
    users = db.relationship("StandardUserModel",
                            secondary=users_digital_books_associations_table,
                            back_populates="digital_books")


class AudioBooksModel(BooksModel):
    __tablename__ = "audio_books"

    reader_name = db.Column(db.String(100), nullable=False)
    # relation between standard users and reading books bidirectional
    users = db.relationship("StandardUserModel",
                            secondary=users_audio_books_associations_table,
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
