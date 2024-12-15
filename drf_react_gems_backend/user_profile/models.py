from django.db import models

from drf_react_gems_backend.user_credentials.models import (
    UserCredentials,
)

from drf_react_gems_backend.common.models import BaseUserCharField

from drf_react_gems_backend.user_profile.constants import (
    NAME_RULES,
)


class UserProfile(models.Model):

    first_name = BaseUserCharField.create_char_field(
        max_length=NAME_RULES["max_length"],
        pattern=NAME_RULES["pattern"],
        pattern_error_message=NAME_RULES["pattern_error_message"],
        null_value=NAME_RULES["null"],
        blank_value=NAME_RULES["blank"],
    )

    last_name = BaseUserCharField.create_char_field(
        max_length=NAME_RULES["max_length"],
        pattern=NAME_RULES["pattern"],
        pattern_error_message=NAME_RULES["pattern_error_message"],
        null_value=NAME_RULES["null"],
        blank_value=NAME_RULES["blank"],
    )

    user = models.OneToOneField(
        to=UserCredentials,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="user_profile",
    )
