from marshmallow import fields, validate, Schema

from schemas.base import AuthBaseSchema
from utils.validators import validate_password


class RegisterSchemaRequest(AuthBaseSchema):
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    first_name = fields.Str(required=True, validate=validate.Length(min=3, max=35))
    last_name = fields.Str(required=True, validate=validate.Length(min=3, max=35))


class LoginSchemaRequest(AuthBaseSchema):
    pass


class UpdateSchemaRequest(Schema):
    email = fields.Email(allow_none=True)
    password = fields.Str(allow_none=True, validate=validate.And(validate_password, validate.Length(min=8, max=32)))
    username = fields.Str(allow_none=True, validate=validate.Length(min=3, max=50))
    first_name = fields.Str(allow_none=True, validate=validate.Length(min=3, max=35))
    last_name = fields.Str(allow_none=True, validate=validate.Length(min=3, max=35))
