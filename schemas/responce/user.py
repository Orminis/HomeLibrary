from marshmallow import fields, Schema


class UserSchemaResponse(Schema):
    username = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
