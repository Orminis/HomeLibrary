from marshmallow import fields, Schema, validate

from utils.validators import validate_password


class RegisterSchemaRequest(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    first_name = fields.Str(required=True, validate=validate.Length(min=3, max=35))
    last_name = fields.Str(required=True, validate=validate.Length(min=3, max=35))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.And(validate_password, validate.Length(min=8, max=32)))


# class LoginSchemaRequest(Schema):
#     # TODO login with username or email
#     username_or_email = fields.Str(required=True, validate=validate.OneOf())
#     password = fields.Str(required=True, validate=validate.And(validate_password, validate.Length(min=8, max=32)))
