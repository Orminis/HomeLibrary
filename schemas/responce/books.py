from marshmallow import fields

from schemas.base import BookBaseSchema


class ReadingBooksSchemaResponse(BookBaseSchema):
    photo_url = fields.Str(required=True)


class DigitalBooksSchemaResponse(BookBaseSchema):
    photo_url = fields.Str(required=True)


class AudioBooksSchemaResponse(BookBaseSchema):
    photo_url = fields.Str(required=True)

