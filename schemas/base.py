from marshmallow import Schema, fields, validate

from utils.validators import validate_password, validate_isbn, validate_name


class AuthBaseSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(
        required=True,
        validate=validate.And(validate_password, validate.Length(min=8, max=32)),
    )


class BookBaseSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=2, max=255))
    author_name = fields.Str(
        required=True,
        validate=validate.And(validate_name, validate.Length(min=7, max=100)),
    )
    isbn = fields.Integer(required=True, validate=validate_isbn)
