from django.core.exceptions import ValidationError

def check_length(value):
    value = str(value)

    if len(value) < 8:
        raise ValidationError("طول پسورد نمیتواند کمتر از 8 باشد")

