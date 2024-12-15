from django.db import (
    models,
)
from django.core.validators import (
    RegexValidator,
    MinLengthValidator,
)


class BaseUserCharField(models.Model):
    class Meta:
        abstract = True

    @staticmethod
    def create_char_field(
        max_length: int,
        pattern: str,
        pattern_error_message: str,
        null_value: bool,
        blank_value: bool,
    ) -> models.CharField:

        return models.CharField(
            max_length=max_length,
            error_messages={
                "blank": "This field is required",
                "max_length": f"This field must not exceed {max_length} characters",
            },
            validators=[
                RegexValidator(
                    regex=pattern,
                    message=pattern_error_message,
                ),
            ],
            null=null_value,
            blank=blank_value,
        )
