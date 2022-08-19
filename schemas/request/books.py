from marshmallow import fields, validate, Schema

from utils.validators import validate_format_cover


class RegisterBookSchemaRequest(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2, max=255))
    author_first_name = fields.Str(required=True, validate=validate.Length(min=2, max=35))
    author_last_name = fields.Str(required=True, validate=validate.Length(min=2, max=35))
    genre = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    description = fields.Raw(required=True)
    comments = fields.Raw(allow_none=True)


class ReadingBookSchemaRequest(RegisterBookSchemaRequest):
    original_language = fields.Str(allow_none=True, validate=validate.Length(min=2, max=20))
    publish_language = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    edition = fields.Int(required=True)
    paper_format_cover = fields.Str(allow_none=True, validate=validate.And(validate_format_cover,
                                                                           validate.Length(min=4, max=4)))
    digital_format = fields.Bool()


class AudioBookSchemaRequest(RegisterBookSchemaRequest):
    reader_name = fields.Str(required=True, validate=validate.Length(min=5, max=100))
