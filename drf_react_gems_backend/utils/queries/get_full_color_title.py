from django.db.models import (
    Case,
    When,
    Value,
    CharField,
)


def get_full_color_title():
    return Case(
        When(product__color__title="P", then=Value("Pink Sapphire")),
        When(product__color__title="B", then=Value("Blue Sapphire")),
        When(product__color__title="W", then=Value("Brilliant Diamond")),
        default=Value("Unknown Color"),
        output_field=CharField(),
    )
