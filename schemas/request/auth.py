from marshmallow import fields, Schema, validate

from schemas.base import AuthBaseSchema


class RegisterSchemaRequest(AuthBaseSchema):
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    first_name = fields.Str(required=True, validate=validate.Length(min=3, max=35))
    last_name = fields.Str(required=True, validate=validate.Length(min=3, max=35))


class LoginSchemaRequest(AuthBaseSchema):
    pass
