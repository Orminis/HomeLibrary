from flask import request
from werkzeug.exceptions import BadRequest, Forbidden

from managers.auth import auth


def validate_schema(schema_name):
    def decorated_function(func):
        def wrapper(*args, **kwargs):
            data = request.get_json()
            schema = schema_name()
            errors = schema.validate(data)
            if not errors:
                return func(*args, **kwargs)
            raise BadRequest(errors)
        return wrapper
    return decorated_function


# decorator for permitted roles.
def permission_required(*roles):
    def decorated_function(func):
        def wrapper(*args, **kwargs):
            token_user = auth.current_user()
            approved_roles = (role for role in roles)
            if token_user.role not in approved_roles:
                raise Forbidden("Permission denied!")
            return func(*args, **kwargs)
        return wrapper
    return decorated_function
