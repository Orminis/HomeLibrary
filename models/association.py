from db import db
from models.enum import Condition


class UsersReadingBooksAssociations(db.Model):
    __tablename__ = "users_reading_books_associations"

    # TODO condition column & rating column
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("standard_user.id"))
    reading_book_id = db.Column(db.Integer, db.ForeignKey("reading_books.id"))
    user_comments = db.Column(db.Text, nullable=False)
    user_rating = db.Column(db.Integer, nullable=False)
    user_condition = db.Column(db.Enum(Condition), default=Condition.very_good, nullable=False)


class UsersDigitalBooksAssociations(db.Model):
    __tablename__ = "users_digital_books_associations"

    # TODO condition column & rating column
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("standard_user.id"))
    digital_book_id = db.Column(db.Integer, db.ForeignKey("digital_books.id"))
    user_comments = db.Column(db.Text, nullable=False)
    user_rating = db.Column(db.Integer, nullable=False)


class UsersAudioBooksAssociations(db.Model):
    __tablename__ = "users_audio_books_associations"

    # TODO condition column & rating column
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("standard_user.id"))
    audio_book_id = db.Column(db.Integer, db.ForeignKey("audio_books.id"))
    user_comments = db.Column(db.Text, nullable=False)
    user_rating = db.Column(db.Integer, nullable=False)
