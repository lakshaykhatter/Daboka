from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import re


@deconstructible
class UsernameValidator(validators.RegexValidator):
    """
    Validator for usernames.

    - Only ASCII lowercase letters, numbers and underscore are supported.
    - Must start with a letter.
    """
    # regex = r'^[a-z][a-z0-9_]+$'
    regex = r'^[0-9a-z_]*$'
    message = _(
        'Enter a valid username. This value may contain only lowercase ASCII letters, '
        'numbers, and underscores. Must start with a letter.'
    )
    flags = 0