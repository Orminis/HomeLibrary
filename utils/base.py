import base64

from werkzeug.exceptions import BadRequest


def decode_file(path, encoded_file):
    with open(path, "wb") as decode:
        try:
            decode.write(base64.b64decode(encoded_file.encode("utf-8")))
        except Exception as ex:
            raise BadRequest("Invalid photo encoding")
