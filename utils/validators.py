from marshmallow import ValidationError
from password_strength import PasswordPolicy

# Определяне на условия за паролите чрез password_strength

policy = PasswordPolicy.from_names(
    uppercase=1,  # need min. 1 uppercase letters
    numbers=1,  # need min. 1 digits
    special=1,  # need min. 1 special characters
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
    if len(isbn) < 10 or len(isbn) > 13:
        raise ValidationError("Input correct ISBN!")
