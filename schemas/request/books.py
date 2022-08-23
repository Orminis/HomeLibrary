from marshmallow import fields, validate, Schema

from utils.validators import validate_format_cover, validate_name


class RegisterBookSchemaRequest(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=2, max=255))
    author_name = fields.Str(required=True, validate=validate.And(validate_name, validate.Length(min=7, max=100)))
    genre = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    description = fields.Raw(required=True)
    comments = fields.Raw(allow_none=True)
    isbn = fields.Integer(required=True, validate=validate.Length(min=10, max=13))


class ReadingBookSchemaRequest(RegisterBookSchemaRequest):
    original_language = fields.Str(allow_none=True, validate=validate.Length(min=2, max=20))
    publish_language = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    edition = fields.Int(required=True)
    paper_format_cover = fields.Str(allow_none=True,
                                    validate=validate.And(validate_format_cover, validate.Length(min=4, max=4)))


class DigitalBooksSchemaRequest(RegisterBookSchemaRequest):
    original_language = fields.Str(allow_none=True, validate=validate.Length(min=2, max=20))
    publish_language = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    edition = fields.Int(required=True)


class AudioBookSchemaRequest(RegisterBookSchemaRequest):
    reader_name = fields.Str(required=True, validate=validate.Length(min=5, max=100))
