from marshmallow import fields

from schemas.base import BookBaseSchema


class ReadingBooksSchemaResponse(BookBaseSchema):
    cover_photo_url = fields.Str(required=True)


class DigitalBooksSchemaResponse(BookBaseSchema):
    cover_photo_url = fields.Str(required=True)


class AudioBooksSchemaResponse(BookBaseSchema):
    cover_photo_url = fields.Str(required=True)
