from django.core.exceptions import ValidationError

def validate_secure_passoword(value):
    if len(value)<8:
        raise ValidationError("Password Can't be Less then 8 carector")
    