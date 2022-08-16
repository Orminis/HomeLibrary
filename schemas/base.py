from marshmallow import Schema, fields, validate

from utils.validators import validate_password


class AuthBaseSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.And(validate_password, validate.Length(min=8, max=32)))
