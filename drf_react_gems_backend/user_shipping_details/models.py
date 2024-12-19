from django.db import (
    models,
)

from cities_light.models import (
    City,
    Country,
    Region,
)

from drf_react_gems_backend.common.models import BaseUserCharField

from drf_react_gems_backend.user_credentials.models import UserCredentials

from drf_react_gems_backend.user_shipping_details.constants import (
    FIRST_NAME_RULES,
    LAST_NAME_RULES,
    PHONE_NUMBER_RULES,
    STREET_ADDRESS_RULES,
    APARTMENT_RULES,
    POSTAL_CODE_RULES,
)


class UserShippingDetails(BaseUserCharField):
    class Meta:
        verbose_name_plural = "User Shipping Details"

    first_name = BaseUserCharField.create_char_field(
        max_length=FIRST_NAME_RULES["max_length"],
        pattern=FIRST_NAME_RULES["pattern"],
        pattern_error_message=FIRST_NAME_RULES["pattern_error_message"],
        null_value=FIRST_NAME_RULES["null"],
        blank_value=FIRST_NAME_RULES["blank"],
    )

    last_name = BaseUserCharField.create_char_field(
        max_length=LAST_NAME_RULES["max_length"],
        pattern=LAST_NAME_RULES["pattern"],
        pattern_error_message=LAST_NAME_RULES["pattern_error_message"],
        null_value=LAST_NAME_RULES["null"],
        blank_value=LAST_NAME_RULES["blank"],
    )

    phone_number = BaseUserCharField.create_char_field(
        max_length=PHONE_NUMBER_RULES["max_length"],
        pattern=PHONE_NUMBER_RULES["pattern"],
        pattern_error_message=PHONE_NUMBER_RULES["pattern_error_message"],
        null_value=PHONE_NUMBER_RULES["null"],
        blank_value=PHONE_NUMBER_RULES["blank"],
    )

    country = models.ForeignKey(
        to=Country,
        on_delete=models.DO_NOTHING,
        default="",
        null=True,
        blank=True,
    )

    city = models.ForeignKey(
        to=City,
        on_delete=models.DO_NOTHING,
        default="",
        null=True,
        blank=True,
    )

    street_address = BaseUserCharField.create_char_field(
        max_length=STREET_ADDRESS_RULES["max_length"],
        pattern=STREET_ADDRESS_RULES["pattern"],
        pattern_error_message=STREET_ADDRESS_RULES["pattern_error_message"],
        null_value=STREET_ADDRESS_RULES["null"],
        blank_value=STREET_ADDRESS_RULES["blank"],
    )

    apartment = BaseUserCharField.create_char_field(
        max_length=APARTMENT_RULES["max_length"],
        pattern=APARTMENT_RULES["pattern"],
        pattern_error_message=APARTMENT_RULES["pattern_error_message"],
        null_value=APARTMENT_RULES["null"],
        blank_value=APARTMENT_RULES["blank"],
    )

    postal_code = BaseUserCharField.create_char_field(
        max_length=POSTAL_CODE_RULES["max_length"],
        pattern=POSTAL_CODE_RULES["pattern"],
        pattern_error_message=POSTAL_CODE_RULES["pattern_error_message"],
        null_value=POSTAL_CODE_RULES["null"],
        blank_value=POSTAL_CODE_RULES["blank"],
    )

    user = models.OneToOneField(
        to=UserCredentials,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="user_shipping_details",
    )
