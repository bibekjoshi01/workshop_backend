from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

from config import settings


def validate_image(image):
    file_size = image.size
    limit_byte_size = settings.MAX_UPLOAD_SIZE
    if file_size > limit_byte_size:
        # converting into kb
        f = limit_byte_size / 1024
        # converting into MB
        f = f / 1024
        error_message = f"Max size of file is {f} MB"
        raise ValidationError(error_message)


@deconstructible
class CustomUsernameValidator(validators.RegexValidator):
    regex = r"^[a-zA-Z0-9_]+$"
    message = _(
        "Enter a valid username. This value may only contain letters, "
        "numbers, and underscores.",
    )
    flags = 0
