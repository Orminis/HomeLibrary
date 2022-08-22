from db import db


class AuthorsModel(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(35), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    nationality = db.Column(db.String(50), nullable=False)

    # Author's books association
    reading_books_id = db.Column(db.Integer, db.ForeignKey("reading_books.id"))
    reading_books = db.relationship("ReadingBooksModel", backref="author")
    digital_books_id = db.Column(db.Integer, db.ForeignKey("digital_books.id"))
    digital_books = db.relationship("DigitalBooksModel", backref="author")
    audio_books_id = db.Column(db.Integer, db.ForeignKey("audio_books.id"))
    audio_books = db.relationship("AudioBooksModel", backref="author")
