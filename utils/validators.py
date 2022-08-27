from marshmallow import ValidationError
from password_strength import PasswordPolicy

# Определяне на условия за паролите чрез password_strength
from werkzeug.exceptions import BadRequest

from models import StandardUserModel

policy = PasswordPolicy.from_names(
    uppercase=2,  # need min. 1 uppercase letters
    numbers=1,  # need min. 1 digits
    special=2,  # need min. 1 special characters
    nonletters=1,  # need min. 1 non-letter characters (digits, specials, anything)
)


def validate_password(password):
    errors = policy.test(password)
    if errors:
        raise ValidationError(f"{errors}")


covers = {"soft": "Soft Cover", "hard": "Hard Cover"}


def validate_format_cover(cover):
    if cover not in covers:
        raise ValidationError(f"Wrong cover!")


def validate_isbn(isbn):
    if len(str(isbn)) < 10 or len(str(isbn)) > 13:
        raise ValidationError("Input correct ISBN!")


def validate_name(name):
    try:
        first_name, last_name = name.split()
    except ValueError:
        raise ValidationError("Please input First and Last Names!")
    if len(first_name) < 2 or len(last_name) < 2:
        raise ValidationError("Each name should contain at least 2 characters!")


# Check if email or username exists in StandardUserModel
def validate_existing_email(email):
    if StandardUserModel.query.filter_by(email=email).first():
        raise BadRequest("Credentials already in use!")


def validate_existing_username(username):
    if StandardUserModel.query.filter_by(username=username).first():
        raise BadRequest("Credentials already in use!")
