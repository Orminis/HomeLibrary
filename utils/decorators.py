from flask import request
from werkzeug.exceptions import BadRequest, Forbidden

from managers.auth import auth
from models import StandardUserModel


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


def permission_required(*roles):
    def decorated_function(func):
        def wrapper(*args, **kwargs):
            curr_user = StandardUserModel.query.filter_by(id=kwargs["user_id"]).first()
            curr_role = curr_user.role
            approved_roles = (role for role in roles)
            if curr_role not in approved_roles:
                raise Forbidden("Permission denied!")
            return func(*args, **kwargs)
        return wrapper
    return decorated_function
